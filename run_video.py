"""
Запуск прототипа для классификации направления взгляда водителя на видео

@author Sergey Vakhrameev
"""
from src.analysis import ImageGazePredictor
import cv2
import click


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
def main(input_filepath):
    cap = cv2.VideoCapture(input_filepath)
    ana = ImageGazePredictor(sliding_window_size=2)

    if (cap.isOpened() == False):
        print("Ошибка открытия видеофайла")
    else:
        print(1)
        # раскомментируй все, что ниже для сохранения обработанного видео в файл
        # fps = cap.get(5)
        # frame_count = cap.get(7)
        # frame_width = int(cap.get(3))
        # frame_height = int(cap.get(4))
        # frame_size = (frame_width,frame_height)

        # output = cv2.VideoWriter('processed_video.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 20, frame_size)

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                processed_frame = ana.track_gaze(frame)
                cv2.imshow('Frame', processed_frame)
                cv2.waitKey(1)
                # output.write(processed_frame)
            else:
                break

        cap.release()
        # output.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
