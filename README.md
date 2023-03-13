<h1 align="center">Driver Gaze Predictor</h1>

<p align="center">
  <img src="demo.gif" alt="animated" />
</p>

# Русская версия
## Описание:

Модель для определения направления взгляда водителя. 
Возможные входные данные:
    - Путь к изображению (run_frame.py);
    - Путь к видео (run_video.py);
    - Изображения с веб-камеры для запуска в режиме реального времени (run_webcam).

Классы:
- 0 - 'левая верхняя часть лобового стекла',
- 1 - 'прямо перед собой',
- 2 - 'спидометр', 
- 3 - 'радио',
- 4 - 'правая верхняя часть лобового стекла',
- 5 - 'правая нижняя часть лобового стекла', 
- 6 - 'правое боковое зеркало', 
- 7 - 'зеркало заднего вида', 
- 8 - 'левое боковое зеркало'.

Точность модели на датасете <a href='https://sites.google.com/view/drivergazeprediction/home?pli=1'>DGW</a> составляет 65.85% и 64.19% на валидационной и тестовой выборках соответственно. Доступ к официальной тестовой выборке был утерян, поэтому она была получена из тренировочной выборки. Разделение кадров на 3 выборки представлено в директории dgw_annotation, там размещены .pickle файлы.

Ссылка на список экспериментов при обучении модели: https://docs.google.com/spreadsheets/d/1mxy4Okgb4FoaO_F6x-o7Jy1WDVrNDcsX8hAvSUKrdZg/edit?usp=sharing.

Протестировать можно по следующей ссылке: https://ai.m16.tech/api/cnn_based_driver_gaze_predictor?image_path=https://disk.yandex.ru/i/gzOQr0EMeagXtw
где https://disk.yandex.ru/i/gzOQr0EMeagXtw - путь к изображению на яндекс диске. Доступ к изображению должен быть открыт к чтению для всех, у кого есть ссылка.

Данная модель очень чувствительна к ракурсу, с которого сделан снимок. Ее точность напрямую зависит от местоположения камеры. Для получения оптимальной точности распознавания камеру следует расположить примерно так же, как в датасете DGW или на GIF-ке выше.

Для запуска прототипа локально вам необходимо установить библиотеки, указанные в файле requirements.txt. Затем из корня проекта запустить один из python файлов (run_frame.py, run_video.py, run_webcam.py), предварительно заменив существующие пути к файлам в коде на свои.

<br>

# English version
## Description:

Model for determining the direction of the driver's gaze. 
Possible input data:
    - Image path (run_frame.py);
    - Video path (run_video.py);
    - A sequence of frames from a webcam for real-time use (run_webcam).

Classes:
- 0 - 'upper left part of the windshield',
- 1 - 'straight',
- 2 - 'speedometer', 
- 3 - 'radio',
- 4 - 'upper right part of the windshield',
- 5 - 'bottom right part of the windshield', 
- 6 - 'right side mirror', 
- 7 - 'rear view mirror', 
- 8 - 'left side mirror'.

Accuracy of the model on the <a href='https://sites.google.com/view/drivergazeprediction/home?pli=1'>DGW</a> dataset is 65.85% and 64.19% on the validation and test sets, respectively. Access to the official test set was lost, so it was obtained from the training set. The division of frames into 3 sets is presented in the dgw_annotation directory, where .pickle files are placed (the content of the .pickle files is in the pandas DataFrame format with the "Frame name" and "Class" columns).

Link to the list of experiments when training the model: https://docs.google.com/spreadsheets/d/1mxy4Okgb4FoaO_F6x-o7Jy1WDVrNDcsX8hAvSUKrdZg/edit?usp=sharing.

You can test the operation of the model using the following link: https://ai.m16.tech/api/cnn_based_driver_gaze_predictor?image_path=https://disk.yandex.ru/i/gzOQr0EMeagXtw
where https://disk.yandex.ru/i/gzOQr0EMeagXtw - the path to the image on Yandex Disk. Access to the image should be open to reading for everyone who has a link.

This model is very sensitive to the angle from which the picture was taken. Its accuracy directly depends on the location of the camera. To obtain optimal recognition accuracy, the camera should be positioned approximately the same as in the DGW dataset or in the GIF above.

To run the prototype locally on your computer, you need to install the libraries specified in the file requirements.txt . Then run one of the python files from the root of the project (run_frame.py , run_video.py , run_webcam.py ), having previously replaced the existing file paths in the code with their own.