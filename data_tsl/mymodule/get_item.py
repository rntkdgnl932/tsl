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

from clean_screen import all_skip, skip_check, skip_start, clean_screen_start
from check import out_check
from function_game import click_pos_2, click_pos_reg, imgs_set_, imgs_set_for, drag_pos
from schedule import myQuest_play_add

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')
# C:\my_games\tsl\data_tsl\imgs\get_item\event\event_title
kind_event_ready = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\event\\event_title\\"
kind_event = os.listdir(kind_event_ready)

kind_point_ready = "c:\\my_games\\tsl\\data_tsl\\imgs\\point\\"


def get_item_start(cla):
    print("get_item_start")
    get_post(cla)
    get_event(cla, "event")
    get_event(cla, "special")
    get_sangjum(cla)

def get_post(cla):
    print("get_post")

    is_ing = True
    is_ing_count = 0
    while is_ing is True:

        is_ing_count += 1

        if is_ing_count > 20:
            is_ing = False

        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\post.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 200, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("post", imgs_)

            is_point = False
            point_ready = kind_point_ready + "post\\"
            point_ = os.listdir(point_ready)
            for p in range(len(point_)):
                full_path = str(point_ready) + point_[p]
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 60, 360, 120, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("post point!!!!!", point_[p], imgs_)
                    is_point = True
                    click_pos_reg(imgs_.x - 25, imgs_.y + 10, cla)
                    QTest.qWait(500)
                    break

            if is_point == True:

                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\post\\get_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(870, 960, 1010, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("get_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(1000)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)
                    skip_start(cla)
            else:
                is_ing = False

        else:

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\post.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 30, 1010, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("post", imgs_)
                x_ = imgs_.x
                y_ = imgs_.y

                is_point = False
                point_ready = kind_point_ready + "menu\\"
                point_ = os.listdir(point_ready)
                for p in range(len(point_)):
                    full_path = str(point_ready) + point_[p]
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_, y_ - 40, x_ + 40, y_, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("menu point!!!!!", point_[p], imgs_)
                        is_point = True
                        click_pos_reg(x_, y_, cla)
                        QTest.qWait(500)
                        break
                if is_point == False:
                    is_ing = False

            else:
                menu_open(cla)
        QTest.qWait(1000)

def get_event(cla, data):
    print("get_event", data)

    is_ing = True
    is_ing_count = 0
    while is_ing is True:

        is_ing_count += 1

        if is_ing_count > 10:
            is_ing = False

        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\" + str(data) + ".PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 300, 600, 400, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("event", imgs_)

            point_ready = kind_point_ready + "event\\left\\"
            point_ = os.listdir(point_ready)
            for p in range(len(point_)):

                full_path = str(point_ready) + point_[p]
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(270, 370, 320, 740, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("event left point...1", point_[p], imgs_)

                    get_event_click(cla)

                    break
            else:
                is_event = False

                point_ready = kind_point_ready + "event\\left\\"
                point_ = os.listdir(point_ready)
                for p in range(len(point_)):

                    full_path = str(point_ready) + point_[p]
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(270, 370, 320, 740, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("event left point...2", point_[p], imgs_)
                        is_event = True
                        break

                if is_event == False:

                    if str(data) == "event":
                        drag_pos(230, 650, 230, 400, cla)
                        QTest.qWait(500)
                        for p in range(len(point_)):

                            full_path = str(point_ready) + point_[p]
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(270, 370, 320, 740, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("event left point...2", point_[p], imgs_)
                                is_event = True
                                break


                if is_event == False:
                    is_ing = False

        else:

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\" + str(data) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 30, 1010, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("event kind", str(data), imgs_)
                x_ = imgs_.x
                y_ = imgs_.y

                is_point = False
                point_ready = kind_point_ready + "menu\\"
                point_ = os.listdir(point_ready)
                for p in range(len(point_)):
                    full_path = str(point_ready) + point_[p]
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_, y_ - 40, x_ + 40, y_, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("menu point!!!!!", point_[p], imgs_)
                        is_point = True
                        click_pos_reg(x_, y_, cla)
                        QTest.qWait(500)
                        break
                if is_point == False:
                    is_ing = False


            else:
                menu_open(cla)
        QTest.qWait(1000)



def get_event_click(cla):

    print("get_event_click")

    is_ing = True
    is_ing_count = 0
    while is_ing is True:
        is_ing_count += 1

        if is_ing_count > 20:
            is_ing = False
        ##################################################
        ###############이벤트 종류 정하기#########################
        ##################################################

        is_point = False
        kind = "none"
        x_reg = 0
        y_reg = 0
        point_ready = kind_point_ready + "event\\left\\"
        point_ = os.listdir(point_ready)
        for p in range(len(point_)):

            full_path = str(point_ready) + point_[p]
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(270, 370, 320, 740, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("event point!!!!!", point_[p], imgs_)
                is_point = True

                x_reg = imgs_.x
                y_reg = imgs_.y
                click_pos_reg(x_reg - 50, y_reg + 10, cla)
                QTest.qWait(500)
                click_pos_reg(x_reg - 50, y_reg + 10, cla)
                QTest.qWait(500)

                break

        if is_point == True:
            for i in range(len(kind_event)):
                full_path = str(kind_event_ready) + str(kind_event[i])
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(310, 350, 880, 740, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("kind_event", str(kind_event[i]), imgs_)

            ####################################################
            ##################종류#######################
            ##################################################

                    # - : ?

                    # 1 : pc전용7일출석이벤트(seven) o

                    # 2 : 14일출석이벤트(fourteen) o

                    # 3 : 성장지원이벤트(eight) o

                    # 4 : 특별미션이벤트(eight) o

                    # 5 : 영웅지원이벤트I(seven_four) o

                    # 6 : 보스토벌이벤트(eight) 6

                    # 7 : 영웅지원이벤트(seven_four) 7

                    # 8 : 기본성장시즌패스(all_get) 8

                    # 9 : 기본성장시즌패스(all_get) 8

                    # 10 :

                    # ? : 보스토벌이벤트(eight) 6
                    # ? : 영웅지원이벤트(seven_four) 7

                    # eight => six 포함

                    get_data = kind_event[i].split(".")[0]

                    if get_data == "8" or get_data == "9":
                        kind = "all_get"
                    elif get_data == "1":
                        kind = "seven"

                    elif get_data == "3" or get_data == "4" or get_data == "6":
                        kind = "eight"

                    elif get_data == "2":
                        kind = "fourteen"

                    elif get_data == "5" or get_data == "7":
                        kind = "seven_four"
                    break
            ####################################################
            ##################################################
            ##################################################



            if kind == "none":
                print("none")
                exist_point = True
                for i in range(3):

                    point_ready = kind_point_ready + "event\\seven_four\\"
                    point_ = os.listdir(point_ready)
                    for p in range(len(point_)):

                        full_path = str(point_ready) + point_[p]
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(340, 380, 850, 740, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("event seven point", point_[p], imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                            QTest.qWait(500)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                        else:
                            result_skip = skip_check(cla)
                            if result_skip == True:
                                skip_start(cla)
                            else:
                                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\event\\click_close.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(590, 350, 640, 400, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("click_close", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:

                                    point_ready = kind_point_ready + "event\\left\\"
                                    point_ = os.listdir(point_ready)
                                    for end in range(len(point_)):

                                        full_path = str(point_ready) + point_[end]
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(x_reg - 20, y_reg - 20, x_reg + 20, y_reg + 20, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("exist point", point_[end], imgs_)
                                        else:
                                            exist_point = False
                                            break
                        if exist_point == False:
                            break

                        QTest.qWait(100)
                    QTest.qWait(200)

            elif kind == "all_get":
                print("all_get")

                for i in range(3):
                    exist_point = True
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\event\\all_get_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 600, 830, 740, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("event all_get_btn", point_[p], imgs_)
                        click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                        QTest.qWait(500)
                        click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                    else:
                        result_skip = skip_check(cla)
                        if result_skip == True:
                            skip_start(cla)
                        else:
                            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\event\\click_close.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(590, 350, 640, 400, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("click_close", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                point_ready = kind_point_ready + "event\\left\\"
                                point_ = os.listdir(point_ready)
                                for end in range(len(point_)):

                                    full_path = str(point_ready) + point_[end]
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x_reg - 20, y_reg - 20, x_reg + 20, y_reg + 20, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("exist point", point_[end], imgs_)
                                    else:
                                        print("not exist point")
                                        exist_point = False
                                        break
                    if exist_point == False:
                        break
                    QTest.qWait(100)
                QTest.qWait(200)

            elif kind == "seven":
                print("seven")

                for i in range(3):
                    exist_point = True
                    point_ready = kind_point_ready + "event\\seven\\"
                    point_ = os.listdir(point_ready)
                    for p in range(len(point_)):

                        full_path = str(point_ready) + point_[p]
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(405, 580, 830, 630, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("event seven point", point_[p], imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                            QTest.qWait(500)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                        else:
                            result_skip = skip_check(cla)
                            if result_skip == True:
                                skip_start(cla)
                            else:
                                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\event\\click_close.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(590, 350, 640, 400, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("click_close", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:

                                    point_ready = kind_point_ready + "event\\left\\"
                                    point_ = os.listdir(point_ready)
                                    for end in range(len(point_)):

                                        full_path = str(point_ready) + point_[end]
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(x_reg - 20, y_reg - 20, x_reg + 20, y_reg + 20, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("exist point", point_[end], imgs_)
                                        else:
                                            exist_point = False
                                            break
                        if exist_point == False:
                            break
                        QTest.qWait(100)
                    if exist_point == False:
                        break

                    QTest.qWait(200)



            elif kind == "eight":
                print("eight")
                for i in range(3):
                    exist_point = True
                    point_ready = kind_point_ready + "event\\eight\\"
                    point_ = os.listdir(point_ready)
                    for p in range(len(point_)):

                        full_path = str(point_ready) + point_[p]
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(555, 500, 600, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("event eight point", point_[p], imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                            QTest.qWait(500)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                        else:

                            full_path = str(point_ready) + point_[p]
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 500, 850, 700, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("event eight point", point_[p], imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                                QTest.qWait(500)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                            else:
                                result_skip = skip_check(cla)
                                if result_skip == True:
                                    skip_start(cla)
                                else:
                                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\event\\click_close.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(590, 350, 640, 400, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("click_close", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:

                                        point_ready = kind_point_ready + "event\\left\\"
                                        point_ = os.listdir(point_ready)
                                        for end in range(len(point_)):

                                            full_path = str(point_ready) + point_[end]
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(x_reg - 20, y_reg - 20, x_reg + 20, y_reg + 20, cla,
                                                              img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("exist point", point_[end], imgs_)
                                            else:
                                                exist_point = False
                                                break
                        if exist_point == False:
                            break
                        QTest.qWait(100)
                    if exist_point == False:
                        break



                    QTest.qWait(200)
                for i in range(5):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\event\\click_close.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(590, 350, 640, 400, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("click_close", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    else:
                        click_pos_2(790, 440, cla)
                    QTest.qWait(200)

            elif kind == "fourteen":
                print("fourteen")
                for i in range(3):
                    exist_point = True
                    point_ready = kind_point_ready + "event\\fourteen\\"
                    point_ = os.listdir(point_ready)
                    for p in range(len(point_)):

                        full_path = str(point_ready) + point_[p]
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 500, 830, 540, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("event fourteen point", point_[p], imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                            QTest.qWait(500)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                        else:

                            full_path = str(point_ready) + point_[p]
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 575, 830, 625, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("event fourteen point", point_[p], imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                                QTest.qWait(500)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)

                            else:
                                result_skip = skip_check(cla)
                                if result_skip == True:
                                    skip_start(cla)
                                else:
                                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\event\\click_close.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(590, 350, 640, 400, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("click_close", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        exist_point = True
                                        point_ready = kind_point_ready + "event\\left\\"
                                        point_ = os.listdir(point_ready)
                                        for end in range(len(point_)):

                                            full_path = str(point_ready) + point_[end]
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(x_reg - 20, y_reg - 20, x_reg + 20, y_reg + 20, cla,
                                                              img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("exist point", point_[end], imgs_)
                                            else:
                                                exist_point = False
                                                break
                        if exist_point == False:
                            break
                        QTest.qWait(100)
                    if exist_point == False:
                        break

                    QTest.qWait(200)

            elif kind == "seven_four":
                print("seven_four")
                for i in range(3):
                    exist_point = True
                    point_ready = kind_point_ready + "event\\seven_four\\"
                    point_ = os.listdir(point_ready)

                    is_p = False

                    for p in range(len(point_)):

                        full_path = str(point_ready) + point_[p]
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 490, 860, 540, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("event seven_four point", point_[p], imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                            QTest.qWait(500)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                            is_p = True

                    if is_p == True:
                        for p in range(len(point_)):
                            full_path = str(point_ready) + point_[p]
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(560, 530, 605, 660, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("event seven_four point b1", point_[p], imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                                QTest.qWait(500)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                            else:
                                full_path = str(point_ready) + point_[p]
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(805, 530, 860, 660, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("event seven_four point b2", point_[p], imgs_)
                                    click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                                    QTest.qWait(500)
                                    click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
                            QTest.qWait(100)

                    result_skip = skip_check(cla)
                    if result_skip == True:
                        skip_start(cla)
                    else:
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\event\\click_close.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(590, 350, 640, 400, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("click_close", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:

                            point_ready = kind_point_ready + "event\\left\\"
                            point_ = os.listdir(point_ready)
                            for end in range(len(point_)):

                                full_path = str(point_ready) + point_[end]
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(x_reg - 20, y_reg - 20, x_reg + 20, y_reg + 20, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("exist point", point_[end], imgs_)
                                else:
                                    exist_point = False
                                    break
                    if exist_point == False:
                        break


                    QTest.qWait(200)
                for i in range(5):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\event\\click_close.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(590, 350, 640, 400, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("click_close", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    else:
                        click_pos_2(790, 440, cla)
                    QTest.qWait(200)
        else:
            result_skip = skip_check(cla)
            if result_skip == True:
                skip_start(cla)
            else:
                is_ing = False
        QTest.qWait(1000)


def get_event_sub(cla):
    print("get_event_sub")




def get_upjuk(cla):
    print("get_upjuk")

    is_ing = True
    is_ing_count = 0
    while is_ing is True:

        is_ing_count += 1

        if is_ing_count > 20:
            is_ing = False

        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\upjuk.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 200, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("upjuk", imgs_)

            is_upjuk = False

            point_ready = kind_point_ready + "upjuk\\left\\"
            point_ = os.listdir(point_ready)
            for p in range(len(point_)):

                full_path = str(point_ready) + point_[p]
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(60, 115, 100, 450, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("upjuk point", point_[p], imgs_)
                    click_pos_reg(imgs_.x - 25, imgs_.y + 10, cla)
                    QTest.qWait(500)

                    is_upjuk = True

                    # full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\post\\get_btn.PNG"
                    # img_array = np.fromfile(full_path, np.uint8)
                    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    # imgs_ = imgs_set_(870, 960, 1010, 1040, cla, img, 0.8)
                    # if imgs_ is not None and imgs_ != False:
                    #     print("get_btn", imgs_)
                    #     click_pos_reg(imgs_.x, imgs_.y, cla)
                    #     QTest.qWait(500)
                    #     click_pos_2(940, 1000, cla)
                    #     QTest.qWait(500)
                    #     skip_start(cla)
                else:
                    is_ing = False
            if is_upjuk == True:
                for i in range(20):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\upjuk\\anymore_upjuk.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 90, 640, 140, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("anymore_upjuk", imgs_)
                        break
                    else:
                        click_pos_2(940, 1000, cla)
                    QTest.qWait(300)


        else:

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\upjuk.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 30, 1010, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("upjuk", imgs_)
                x_ = imgs_.x
                y_ = imgs_.y
                is_point = False
                point_ready = kind_point_ready + "menu\\"
                point_ = os.listdir(point_ready)
                for p in range(len(point_)):
                    full_path = str(point_ready) + point_[p]
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_, y_ - 40, x_ + 40, y_, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("menu point!!!!!", point_[p], imgs_)
                        is_point = True
                        click_pos_reg(x_, y_, cla)
                        QTest.qWait(500)
                        break
                if is_point == False:
                    is_ing = False

            else:
                menu_open(cla)
        QTest.qWait(1000)



def get_sangjum(cla):
    print("get_sangjum")

    is_ing = True
    is_ing_count = 0
    while is_ing is True:

        is_ing_count += 1

        if is_ing_count > 20:
            is_ing = False

        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\sangjum.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 200, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("sangjum", imgs_)

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\sangjum\\ilgwal_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 300, 600, 400, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("ilgwal_title", imgs_)

                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\sangjum\\buy.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(490, 660, 630, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("buy", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\sangjum\\anymore_buy_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(370, 90, 700, 150, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("anymore_buy_notice", imgs_)
                            clean_screen_start(cla)
                            is_ing = False
                            break
                        time.sleep(0.1)


            else:
                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\sangjum\\ilgwal_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 970, 150, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("ilgwal_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\sangjum\\anymore_buy_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(370, 90, 700, 150, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("anymore_buy_notice", imgs_)
                            clean_screen_start(cla)
                            is_ing = False
                            break
                        time.sleep(0.1)

        else:

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\sangjum.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 30, 1010, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("post", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

                for i in range(5):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\sangjum.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 200, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    QTest.qWait(300)


            else:
                menu_open(cla)
        QTest.qWait(1000)











