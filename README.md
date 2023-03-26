# unique_img_video
Уникализатор видео и картинок (ffmpeg)

Конфиг подключен не полностью

Используется ffmpeg.exe 

Каталог:
/main.py
/config.ini
/ffmpeg.exe
/input_video/
/input_image/
/output_video/
/output_image/



[Конфиг]

[option_image]
# градус наклона картинки
gradus=3
# ширина
width=1280
# высота
height=760
# растояние от края
borger=25
# Цвет бордера у картинки
borger_color_r=255
borger_color_g=255
borger_color_b=255
# Повернуть изображение по вертикали - горизонтали
flip_LR="False"
# Повернуть изображение по вертикали - горизонтали
flip_TB="False"
# формат изображения
format="png"
# использовать случайные значения
random_config=False
# Удалять исходные изображения
delete_input=False


[option_video]
# Кадров в секунду
fps=24
# Вроде как удаляем мета даду
metadata="-1"
# устанавливаем размер картинки
width_height="hd720"
# Устанавливаем битрейк для видео
bit_m_video="1200k"
# Устанавливаем битрейк для звука
bit_m_audio="128k"
# Обрезать изображение по краям
crop_width=30
# Обрезать изображение по краям
crop_height=20
# затухание музыки
fade=1
#
vibrance=0.05
#
gamma_weight=0.4
#
gamma_r=1
#
gamma_g=1
#
gamma_b=1.2
#
gamma=1
#
saturation=1.02
#
contrast=1.02
#
eq=0.07
# Повернуть видео
rotate=1
# Ускоряем видео
#speed_audio=0
# Ускоряем аудио дорожку
#speed_video=0
#
output="mp4"
# Удалять исходники видео роликов
delete_input=False
# Использовать случайные значения
random_config=False
