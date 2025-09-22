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
from check import out_check, confirm_check
from function_game import click_pos_2, click_pos_reg, imgs_set_, imgs_set_for, drag_pos

kind_point_ready = "c:\\my_games\\tsl\\data_tsl\\imgs\\point\\"


#################

####################
def mission_start(cla, data):

    from potion import potion_check

    try:
        print("mission_start", data)


        result_out = out_check(cla)
        if result_out == True:

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\tuto\\quest_check\\quest_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(940, 850, 1010, 920, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("quest_btn", imgs_)
                potion_check(cla)
            else:
                mission_open(cla, data)
        else:
            mission_open(cla, data)
    except Exception as e:
        print(e)


def mission_open(cla, data):

    from schedule import myQuest_play_add
    from function_game import imgs_set_reg
    mission_kind = data.split("_")
    # mission_kind[1] "1", "2", "3"

    try:

        print("mission_open", data)
        is_ing = True
        is_ing_count = 0
        while is_ing is True:

            is_ing_count += 1

            if is_ing_count > 20:
                is_ing = False

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\mission.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 200, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("quest", imgs_)


                # 보상부터 받기


                for i in range(10):

                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\mission\\bosang_get.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_for = imgs_set_for(350, 540, 650, 650, cla, img, 0.8)
                    if imgs_for is not None and imgs_for != False:
                        if len(imgs_for) > 0:
                            result_ran = random.randint(0, len(imgs_for) - 1)
                            click_pos_reg(imgs_for[result_ran][0], imgs_for[result_ran][1], cla)
                            QTest.qWait(500)

                    result_skip = skip_check(cla)
                    if result_skip == True:
                        skip_start(cla)

                    is_point = False
                    point_ready = kind_point_ready + "mission\\"
                    point_ = os.listdir(point_ready)
                    for p in range(len(point_)):
                        full_path = str(point_ready) + point_[p]
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(45, 65, 265, 120, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("mission : top point!!!!!", point_[p], imgs_)
                            is_point = True
                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                            QTest.qWait(500)
                            break
                    if is_point == True:
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\mission\\mission_clear_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(180, 170, 250, 920, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("mission_clear_1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\mission\\mission_clear_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(180, 170, 250, 920, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("mission_clear_2", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(300)
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\mission\\bosang_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(860, 960, 1010, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("bosang_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            QTest.qWait(500)
                            for r in range(10):
                                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\mission\\bosang_get.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(350, 540, 650, 650, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                QTest.qWait(200)

                    else:
                        break
                    QTest.qWait(500)

                # 미션 얻기
                # 50, 135, 220
                x_reg = (85 * int(mission_kind[1])) - 35
                print("x_reg", x_reg)
                click_pos_2(x_reg, 95, cla)
                QTest.qWait(200)
                click_pos_2(x_reg, 95, cla)
                QTest.qWait(500)

                for i in range(20):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\mission\\any_more_mission_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(365, 85, 640, 140, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("any_more_mission_notice", imgs_)
                        break
                    else:
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\mission\\lack_mission_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(365, 85, 640, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("lack_mission_notice", imgs_)
                            break
                        else:
                            click_pos_2(130, 200, cla)
                            QTest.qWait(200)

                            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\mission\\soolock_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(760, 960, 1010, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("soolock_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(200)

                # 미션 시작하기

                for i in range(5):

                    result_confirm = confirm_check(cla)
                    if result_confirm == True:
                        confirm_all(cla)

                    else:
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\mission.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 30, 200, 200, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\mission\\mission_ing.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(170, 170, 250, 920, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("mission_ing", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)
                                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\tuto\\82_move_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(760, 960, 1010, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("82_move_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                myQuest_play_add(cla, data)
                                break
                        else:

                            break
                    QTest.qWait(500)


                # 미션 타이틀이면 나가기
                for i in range(5):

                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 200, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(990, 55, cla)
                    else:
                        is_ing = False
                        break
                    QTest.qWait(500)





            else:


                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\mission.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 30, 1010, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("menu mission", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                else:
                    menu_open(cla)
            QTest.qWait(1000)


    except Exception as e:
        print(e)