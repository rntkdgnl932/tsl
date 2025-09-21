import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')


from action import menu_open, confirm_all
import numpy as np
import cv2
import pyautogui
import random

from clean_screen import all_skip, skip_check, skip_start, clean_screen_start
from check import out_check
from function_game import click_pos_2, click_pos_reg, imgs_set_, imgs_set_for, drag_pos

kind_point_ready = "c:\\my_games\\tsl\\data_tsl\\imgs\\point\\"


#################

####################
def quest_start(cla, data):


    try:
        print("quest_start", data)

        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\tuto\\jangchak_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 600, 620, 680, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("quest_btn", imgs_)

        all_skip(cla)

        result_out = out_check(cla)
        if result_out == True:

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\tuto\\quest_check\\quest_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(940, 850, 1010, 920, cla, img, 0.8)
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

                    quest_open(cla, data)
        else:
            quest_open(cla, data)
    except Exception as e:
        print(e)


def quest_open(cla, data):

    quest_kind = data.split("_")
    # quest_kind[1] "메인","서브"
    # quest_kind[2] "1", "2", "3"

    try:

        print("quest_open", data)
        is_ing = True
        is_ing_count = 0
        while is_ing is True:

            is_ing_count += 1

            if is_ing_count > 20:
                is_ing = False

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\quest.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 200, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("quest", imgs_)
                # 45, 135, 225
                x_reg = (90 * int(quest_kind[2])) - 45
                click_pos_2(x_reg, 95, cla)
                QTest.qWait(500)

                if data == "메인":
                    click_pos_2(55, 140, cla)
                elif data == "서브":
                    click_pos_2(55, 170, cla)
                QTest.qWait(500)


                point_ready = kind_point_ready + "collection\\item\\"
                point_ = os.listdir(point_ready)
                for p in range(len(point_)):
                    full_path = str(point_ready) + point_[p]
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(270, 120, 320, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("quest : collection item point!!!!!", point_[p], imgs_)
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                        QTest.qWait(500)
                        break


                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\tuto\\bosang_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(860, 960, 1010, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("bosang_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)


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
                    for_1y = 0
                    for_2y = 0
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\tuto\\main_clear_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_for = imgs_set_for(240, 120, 330, 1040, cla, img, 0.8)
                    if imgs_for is not None and imgs_for != False:
                        if len(imgs_for) > 0:
                            for_1x = imgs_for[len(imgs_for) - 1][0]
                            for_1y = imgs_for[len(imgs_for) - 1][1]

                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\tuto\\main_clear_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_for = imgs_set_for(240, 120, 330, 1040, cla, img, 0.8)
                    if imgs_for is not None and imgs_for != False:
                        if len(imgs_for) > 0:
                            for_2x = imgs_for[len(imgs_for) - 1][0]
                            for_2y = imgs_for[len(imgs_for) - 1][1]

                    if for_1y > for_2y:
                        for_x = for_1x
                        for_y = for_1y
                    else:
                        for_x = for_2x
                        for_y = for_2y

                    if for_y > 900:
                        drag_pos(220, 990, 220, 965, cla)
                        QTest.qWait(2000)
                        for i in range(10):
                            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\tuto\\main_clear_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(240, 120, 330, 1040, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                drag_pos(220, 965, 220, 990, cla)
                            QTest.qWait(2000)

                    else:
                        click_pos_reg(for_x, for_y + 45, cla)




            else:
                result_skip = skip_check(cla)
                if result_skip == True:
                    skip_start(cla)


                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\quest.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 30, 1010, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("quest", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    is_not = False
                    is_quest = False
                    for i in range(12):
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\tuto\\not_opened_notice_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(350, 60, 600, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("not_opened_notice_1", imgs_)
                            is_not = True
                            break
                        else:
                            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\quest.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 30, 200, 200, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("quest", imgs_)
                                is_quest = True
                                break
                        time.sleep(0.1)
                    if is_not == True or is_quest == False:
                        clean_screen_start(cla)
                        click_pos_2(960, 100, cla)
                        time.sleep(0.5)
                        confirm_all(cla)

                else:
                    menu_open(cla)
            QTest.qWait(1000)


    except Exception as e:
        print(e)