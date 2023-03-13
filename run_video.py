"""
Запуск прототипа для классификации направления взгляда водителя на видео

@author Sergey Vakhrameev
"""
from src.analysis import ImageGazePredictor
import cv2


cap = cv2.VideoCapture(r'../test_my_face.MOV')
ana = ImageGazePredictor(sliding_window_size=2)

if (cap.isOpened() == False):
    print("Ошибка открытия видеофайла")
else:
    fps = cap.get(5)

    frame_count = cap.get(7)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frame_size = (frame_width,frame_height)

    output = cv2.VideoWriter('my_face_processed.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 20, frame_size)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            processed_frame = ana.track_gaze(frame)
            cv2.imshow('Frame',processed_frame)

            key = cv2.waitKey(1)
            output.write(processed_frame)
        else:
            break

    cap.release()
    output.release()
    cv2.destroyAllWindows()