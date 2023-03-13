"""
Запуск прототипа для классификации направления взгляда водителя на изображении
"""
from src.analysis import ImageGazePredictor
import cv2


ana = ImageGazePredictor()

frame = cv2.imread(r'C:\Users\User\Downloads\goncharov_photo.png')
processed_frame = ana.track_gaze(frame)

cv2.imshow('Frame',processed_frame)
cv2.waitKey(0)
