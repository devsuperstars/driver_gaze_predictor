"""
Запуск прототипа для классификации направления взгляда водителя на изображении

@author Sergey Vakhrameev
"""
from src.analysis import ImageGazePredictor
import cv2
import click


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
def main(input_filepath):
    ana = ImageGazePredictor()

    frame = cv2.imread(input_filepath)
    processed_frame = ana.track_gaze(frame)

    cv2.imshow('Frame',processed_frame)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
