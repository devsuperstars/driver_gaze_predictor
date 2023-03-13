"""
@author Sergey Vakhrameev
"""
import cv2
import numpy as np
import sys
import torch
# import torch.nn as nn
import torchvision
import mtcnn

sys.path.append('src')


class ImageGazePredictor:
    """
    Определитель направления взгляда на изображении
    """
    def __init__(self, sliding_window_size: int = 0):
        self.device = 'cpu' # torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        # загрузка детектора лица
        self.face_detector = mtcnn.MTCNN() # FacialImageProcessing(False)
        # загрузка классификатора
        self.gaze_tracker = self.load_gaze_tracker('src/models/enet_b0_sota.pt')
        # размер скользящего окна для сглаживания предсказаний
        self.sliding_window_size = sliding_window_size 
        self.sliding_window_preds = []
        self.decode_target = {
            0: 'upper left part of the windshield', # 'левая верхняя часть лобового стекла',
            1: 'straight', # 'прямо перед собой',
            2: 'speedometer', #'спидометр',
            3: 'radio', # 'радио',
            4: 'upper right part of the windshield', #'правая верхняя часть лобового стекла',
            5: 'bottom right part of the windshield', #'правая нижняя часть лобового стекла',
            6: 'right side mirror', #'правое боковое зеркало',
            7: 'rear view mirror', #'зеркало заднего вида',
            8: 'left side mirror', #'левое боковое зеркало',
        }

        self.frame_count = 0

    def load_gaze_tracker(self, model_path: str):
        """
        Загрузка модели.
            Вход: путь к модели
            Выход: сама модель
        """
        model = torch.load(model_path, map_location = torch.device('cpu'))
        if self.device == 'cuda:0':
            model.to(self.device)

        model.eval()

        return model

    def track_gaze(self, frame):
        """
        Определение направления взгляда.
            Вход: кадр
            Вызод: кадр с предскзанным классом, либо иным текстом
        """
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        bounding_boxes = self.face_detector.detect_faces(frame_bgr)

        if len(bounding_boxes) == 0:
            return frame

        x, y, width, height = bounding_boxes[0]['box']

        face = frame[y:y+height,x:x+width,:]

        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 0), 1)

        transform = torchvision.transforms.Compose(
            [
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Resize((260, 260)),
                # раскомментировать при работе с веб-камеры:
                # torchvision.transforms.RandomHorizontalFlip(p=1),
            ]
        )

        face_transformed = transform(face)
        face_transformed = torch.unsqueeze(face_transformed, 0)

        if self.device == 'cuda:0':
            face_transformed.to(self.device)

        predicted_gaze_direction = self.gaze_tracker(face_transformed)
        # probs = nn.functional.softmax(predicted_gaze_direction, dim=1)

        predicted_gaze_direction = predicted_gaze_direction.argmax(1).cpu().detach().item()

        if len(self.sliding_window_preds) < self.sliding_window_size:
            self.sliding_window_preds.append(predicted_gaze_direction)
            predicted_gaze_direction = 'Loading...'
        else:
            self.sliding_window_preds = self.sliding_window_preds[1:] + [predicted_gaze_direction]
            predicted_gaze_direction = np.round(np.bincount(self.sliding_window_preds).argmax())
            predicted_gaze_direction = self.decode_target[predicted_gaze_direction]

        cv2.putText(frame, predicted_gaze_direction, (50, 100), self.font, 1, (0, 0, 255), 3)

        return frame
