import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_


from action import menu_open, confirm_all
import numpy as np
import cv2
import pyautogui
import random



sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def dead_die(cla, data):
    from clean_screen import all_skip, skip_check, skip_start, clean_screen_start
    from check import out_check
    from function_game import click_pos_2, click_pos_reg, imgs_set_, imgs_set_for, drag_pos
    from schedule import myQuest_play_add
    print("dead_die", data)

    is_dead = False

    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dead_die\\maul_boohwal_btn.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(300, 900, 700, 1040, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("maul_boohwal_btn", imgs_)
        is_dead = True
    else:
        is_dead = False
        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dead_die\\boohwal_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(180, 30, 300, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("boohwal_btn", imgs_)
            is_dead = True

    if is_dead == True:
        dead_die_recovery(cla)
        if "퀘스트" in data:
            myQuest_play_add(cla, data)

def dead_die_recovery(cla):
    from clean_screen import all_skip, skip_check, skip_start, clean_screen_start
    from check import out_check
    from function_game import click_pos_2, click_pos_reg, imgs_set_, imgs_set_for, drag_pos
    from schedule import myQuest_play_add
    print("dead_die")





    is_ing = True
    is_ing_count = 0
    while is_ing is True:

        is_ing_count += 1

        if is_ing_count > 20:
            is_ing = False

        result_out = out_check(cla)
        if result_out == True:

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dead_die\\bokgoo_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 700, 600, 800, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("bokgoo_btn", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:

                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dead_die\\boohwal_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(180, 30, 300, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("boohwal_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                else:
                    is_ing = False


        else:
            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dead_die\\maul_boohwal_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(300, 900, 700, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("maul_boohwal_btn", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
        QTest.qWait(1000)



