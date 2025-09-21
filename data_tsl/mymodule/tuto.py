import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

kind_point_ready = "c:\\my_games\\tsl\\data_tsl\\imgs\\point\\"

from action import menu_open, confirm_all
import numpy as np
import cv2
import pyautogui
import random

from clean_screen import all_skip
from check import out_check
from function_game import click_pos_2, click_pos_reg, imgs_set_




#################

####################
def tuto_start(cla):


    try:
        print("tuto_start")
        all_skip(cla)

        result_out = out_check(cla)
        if result_out == True:

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\tuto\\quest_check\\quest_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(880, 780, 960, 880, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("quest_btn", imgs_)
            else:
                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\tuto\\q_clear.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(830, 60, 920, 200, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("q_clear", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:

                    quest_open(cla)
        else:
            quest_open(cla)
    except Exception as e:
        print(e)


def quest_open(cla):


    try:
        print("quest_open")
        is_ing = True
        is_ing_count = 0
        while is_ing is True:

            is_ing_count += 1

            if is_ing_count > 7:
                is_ing = False

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\quest.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 200, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("quest", imgs_)

                point_ready = kind_point_ready + "quest\\left\\"
                point_ = os.listdir(point_ready)
                for p in range(len(point_)):
                    full_path = str(point_ready) + point_[p]
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(280, 115, 325, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("quest point!!!!!", point_[p], imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)
                        break



                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\tuto\\soolock_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(860, 960, 1010, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("soolock_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)

                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\tuto\\82_move_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(860, 960, 1010, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("82_move_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)
                    confirm_all(cla)
                    is_ing = False

            else:
                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\quest.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 30, 1010, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("quest", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    is_in = False

                    for i in range(10):
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\quest.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 30, 200, 200, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            is_in = True
                            break
                        QTest.qWait(100)
                    if is_in == False:
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\character_select.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(740, 30, 1010, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(980, 55, cla)
                            QTest.qWait(500)
                            click_pos_2(880, 110, cla)


                else:
                    menu_open(cla)
            QTest.qWait(1000)


    except Exception as e:
        print(e)