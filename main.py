# -*- coding: utf-8 -*-

import os
import time
import random
import requests
import subprocess
import configparser

from PIL import Image
from PIL import ImageOps
from datetime import datetime




class VID_IMG_EDIT():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini", encoding="utf-8")

    def create_folder(self):
        pass

    def main(self):
        print("Начинаем уникализировать картинки")
        #self.edit_images()

        print("Начинаем уникализировать видео")
        self.edit_video_2()


    def edit_images(self):
        list_image = []

        for img in os.walk("input_image"):
            list_image.append(img[2][0])

        for img in list_image:
            print(img)
            im = Image.open("input_image/" + img)  # !

            gradus = self.config.get("option_image", "gradus")
            x = self.config.get("option_image", "width")
            y = self.config.get("option_image", "height")
            border = self.config.get("option_image", "borger")
            borger_color_r = self.config.get("option_image", "borger_color_r")
            borger_color_g = self.config.get("option_image", "borger_color_g")
            borger_color_b = self.config.get("option_image", "borger_color_b")
            stat_flip_LR = self.config.get("option_image", "flip_LR")
            stat_flip_TB = self.config.get("option_image", "flip_TB")
            format = self.config.get("option_image", "format")

            random_config = self.config.get("option_image", "random_config")
            delete_input = self.config.get("option_image", "delete_input")

            if random_config == "True":
                pass

            # Повернуть изображение по вертикали - горизонтали
            if stat_flip_LR == "True":
                im = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

            if stat_flip_TB == "True":
                im = im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

            # Повернуть изображение под градус
            im_rotate = im.rotate(int(gradus)) #!

            # изменяем размер
            new_image = im_rotate.resize((int(x), int(y)))

            # создание нового изображения с белым фоном
            new_image = ImageOps.expand(new_image, border=int(border), fill=(int(borger_color_r), int(borger_color_g), int(borger_color_b))) #!

            # сохранение картинки и выбор формата
            new_image.save(f'output_image/{img}') #! f'lolk.{format}'

            if delete_input == "True":
                pass


    # https://annimon.com/article/3010
    # https://ffmpeg.org/ffmpeg.html
    # https://webhamster.ru/mytetrashare/index/mtb0/14769541153fhn74se36
    def edit_video_2(self):
        list_video = []

        for video in os.walk("input_video"):
            list_video.append(video[2][0])

        for video in list_video:
            fps = self.config.get("option_video", "fps")
            metadata = self.config.get("option_video", "metadata")
            width_height = self.config.get("option_video", "width_height")
            bit_m_audio = self.config.get("option_video", "bit_m_audio")
            bit_m_video = self.config.get("option_video", "bit_m_video")
            crop_width = self.config.get("option_video", "crop_width")
            crop_height = self.config.get("option_video", "crop_height")
            fade = self.config.get("option_video", "fade")
            vibrance = self.config.get("option_video", "vibrance")
            gamma_weight = self.config.get("option_video", "gamma_weight")
            gamma_r = self.config.get("option_video", "gamma_r")
            gamma_g = self.config.get("option_video", "gamma_g")
            gamma_b = self.config.get("option_video", "gamma_b")
            gamma = self.config.get("option_video", "gamma")
            saturation = self.config.get("option_video", "saturation")
            contrast = self.config.get("option_video", "contrast")
            eq = self.config.get("option_video", "eq")
            rotate = self.config.get("option_video", "rotate")
            # speed_audio = self.config.get("option_video", "speed_audio")
            # speed_video = self.config.get("option_video", "speed_video")
            # output = self.config.get("option_video", "output")
            delete_input = self.config.get("option_video", "delete_input")
            random_config = self.config.get("option_video", "random_config")

            if random_config == "True":
                pass

            subprocess.call([
                "ffmpeg", # Программа
                "-i", # указываем откуда брать видео
                f"input_video\\{video}", # видео для уникализации
                # "-map_metadata", metadata, # Вроде как удаляем мета даду
                "-r", fps,  # устанавливаем FPS
                # "-s", width_height, # устанавливаем размер картинки
                # "-b:v", bit_m_video, # Устанавливаем битрейк для видео
                # "-b:a", bit_m_audio,  # Устанавливаем битрейк для звука
                "-vf", f"crop=in_w-{crop_width}:in_h-{crop_height}", # Обрезать изображение по краям
                "-vf", f"fade=in:{fade}", # afade затухание музыки наоборот
                "-vf", f"vibrance={vibrance}", #
                "-vf", f"gamma_weight={gamma_weight}", #
                "-vf", f"gamma_b={gamma_b}", #
                "-vf", f"gamma_g={gamma_g}", #
                "-vf", f"gamma_r={gamma_r}", #
                "-vf", f"gamma={gamma}", #
                "-vf", f"saturation={saturation}", #
                "-vf", f"contrast={contrast}", #
                "-vf", "hflip", # отзеркалить видео по горизонтали
                "-vf", "vflip",  # отзеркалить видео по вертикали
                "-vf", f"eq=brightness={eq}", #
                "-vf", f"rotate={rotate}*PI/180", # Повернуть видео на 1 градусов
                #"-vf", "setpts=0.25*PTS", # Ускоряем видео 0.25 = x4 примерно
                #"-af", "atempo=2", # Ускоряем аудио дорожку 0.5...100
                f"output_video\\{video}"])

            if delete_input == "True":
                pass




if __name__ == "__main__":
    app = VID_IMG_EDIT()
    app.main()