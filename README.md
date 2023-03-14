<p align="center">
  <img src="demo.gif" alt="animated" />
</p>

# <h1 align="center">Детектор внимания водителя / Driver Gaze Predictor</h1>
## Описание

Модель для определения направления взгляда водителя. За основу была взята EfficientNet-B0 из библиотеки <a href="https://github.com/HSE-asavchenko/hsemotion">HSEmotion</a>, предобученная на VGGFace2 и AffectNet. Затем данная модель была дообучена и протестирована на датасете <a href='https://sites.google.com/view/drivergazeprediction/home?pli=1'>DGW</a>. 

Данная модель классифицирует направление взгляда на следующие направления:
- 0 - 'левая верхняя часть лобового стекла',
- 1 - 'прямо перед собой',
- 2 - 'спидометр', 
- 3 - 'радио',
- 4 - 'правая верхняя часть лобового стекла',
- 5 - 'правая нижняя часть лобового стекла', 
- 6 - 'правое боковое зеркало', 
- 7 - 'зеркало заднего вида', 
- 8 - 'левое боковое зеркало'.

Точность модели на датасете <a href='https://sites.google.com/view/drivergazeprediction/home?pli=1'>DGW</a> составляет 65.85% и 64.19% на валидационной и тестовой выборках соответственно. Доступ к официальной тестовой выборке был утерян, поэтому она была получена из тренировочной выборки. 

Разделение кадров на 3 выборки представлено в директории ``dgw_annotation``, там размещены .pickle файлы (содержание .pickle файлов - таблицы pandas с колонками "Название кадра" и "Класс").

Список экспериментов проведенных в ходе определения наилучших гиперпараметров: ``https://docs.google.com/spreadsheets/d/1mxy4Okgb4FoaO_F6x-o7Jy1WDVrNDcsX8hAvSUKrdZg/edit?usp=sharing``.

Код для предобработки, обучения и тестирования модели находится в файле ``notebook.ipynb``.

## Особенности

Данная модель очень чувствительна к ракурсу, с которого сделан снимок. Ее точность напрямую зависит от местоположения камеры. Для получения оптимальной точности распознавания камеру следует расположить примерно так же, как в датасете DGW или на GIF-ке выше.

## Возможные варианты запуска:

1. Онлайн.

    Необходимо перейти по следующей ссылке: ``https://ai.m16.tech/api/cnn_based_driver_gaze_predictor?image_path=https://disk.yandex.ru/i/gzOQr0EMeagXtw``,
    где ``https://disk.yandex.ru/i/gzOQr0EMeagXtw`` - путь к изображению на яндекс диске. Доступ к изображению должен быть открыт к чтению для всех, у кого есть ссылка.

2. Локально.
    
    Для запуска прототипа локально вам необходимо установить библиотеки, указанные в файле requirements.txt. Для этого запустите команду: 

    ```
    pip install -r requirements.txt
    ```

    Затем из корня проекта запустить один из python файлов (run_frame.py, run_video.py, run_webcam.py):

    2.1. Для обработки одного изображения:
    ```
    python run_frame.py 'путь_к_изображению'
    ```
    2.2. Для обработки видео:
    ```
    python run_video.py 'путь_к_видео'
    ```
    2.3. Для обработки серии кадров с веб-камеры (в реальном времени):
    ```
    python run_webcam.py
    ```

<br>

# <h1 align="center">Driver Gaze Predictor</h1>
## Description

Model for determining the direction of the driver's gaze. The model was based on EfficientNet-B0 from the <a href="https://github.com/HSE-asavchenko/hsemotion">HSEmotion</a> library, pre-trained on VGGFace2 and AffectNet. Then this model was further trained and tested on the <a href='https://sites.google.com/view/drivergazeprediction/home?pli=1'>DGW</a> dataset.

The model classifies the direction of view into the following directions:
- 0 - 'upper left part of the windshield',
- 1 - 'straight',
- 2 - 'speedometer', 
- 3 - 'radio',
- 4 - 'upper right part of the windshield',
- 5 - 'bottom right part of the windshield', 
- 6 - 'right side mirror', 
- 7 - 'rear view mirror', 
- 8 - 'left side mirror'.

Accuracy of the model on the <a href='https://sites.google.com/view/drivergazeprediction/home?pli=1'>DGW</a> dataset is 65.85% and 64.19% on the validation and test sets, respectively. Access to the official test set was lost, so it was obtained from the training set. 

The division of frames into 3 sets is presented in the dgw_annotation directory, where .pickle files are placed (the content of the .pickle files is in the pandas DataFrame format with the "Frame name" and "Class" columns).

Link to the list of experiments when training the model: https://docs.google.com/spreadsheets/d/1mxy4Okgb4FoaO_F6x-o7Jy1WDVrNDcsX8hAvSUKrdZg/edit?usp=sharing.

The code for preprocessing, training and testing the model is located in the file ```notebook.ipynb```.

## Specificities

This model is very sensitive to the angle from which the picture was taken. Its accuracy directly depends on the location of the camera. To obtain optimal recognition accuracy, the camera should be positioned approximately the same as in the DGW dataset or in the GIF above.

## Possible ways to launch the application:

1. Online.

    Follow the link: ``https://ai.m16.tech/api/cnn_based_driver_gaze_predictor?image_path=https://disk.yandex.ru/i/gzOQr0EMeagXtw``,
    where https://disk.yandex.ru/i/gzOQr0EMeagXtw - the path to the image on Yandex Disk. Access to the image should be open to reading for everyone who has a link.

2. Locally on your computer.
    
    To run the prototype locally, you need to install the libraries specified in the file requirements.txt . To do this, run the command: 

    ```
    pip install -r requirements.txt
    ```

    Then run one of the python files from the root of the project (run_frame.py, run_video.py, run_webcam.py):

    2.1. To process a single image:
    ```
    python run_frame.py 'path_to_the_image'
    ```
    2.2. To process a video :
    ```
    python run_video.py 'path_to_the_video'
    ```
    2.3. To process a series of frames from a webcam (real time):
    ```
    python run_webcam.py
    ```