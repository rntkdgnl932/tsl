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
from check import out_check, attack_check, juljun_check
from action import attack_on, juljun_on, go_random
from function_game import click_pos_2, click_pos_reg, imgs_set_, imgs_set_for, drag_pos
from schedule import myQuest_play_add
from potion import potion_check

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')
# C:\my_games\tsl\data_tsl\imgs\get_item\event\event_title
kind_event_ready = "c:\\my_games\\tsl\\data_tsl\\imgs\\get_item\\event\\event_title\\"
kind_event = os.listdir(kind_event_ready)

kind_point_ready = "c:\\my_games\\tsl\\data_tsl\\imgs\\point\\"


def dungeon_start(cla, data):
    # data = 던전_특수_버려진기지, 귀사당,, 별의낙원__4
    dun_data = data.split("_")
    dun_cate_ready = dun_data[1]
    dun_kind = dun_data[2]
    dun_step = dun_data[3]

    if dun_cate_ready == "특수":
        dun_cate = "special"
    elif dun_cate_ready == "파티":
        dun_cate = "party"
    if dun_kind == "버려진기지":
        dun_name = "giji"
    elif dun_kind == "귀사당":
        dun_name = "sadang"
    elif dun_kind == "별의낙원":
        dun_name = "star"
    elif dun_kind == "버려진광산":
        dun_name = "sab"
    elif dun_kind == "달빛사원":
        dun_name = "sawon"
    elif dun_kind == "제르비나의석상":
        dun_name = "jerbana"
    try:
        print("dungeon_start", data)

        result_juljun = juljun_check(cla)
        if result_juljun == True:

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dungeon\\" + str(dun_cate) + "\\" + str(
                dun_name) + "\\" + "juljun_dun_in.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(25, 100, 215, 145, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dungeon juljun_dun_in", str(dun_name), imgs_)

                result_attack = attack_check(cla)
                if result_attack == True:

                    potion_check(cla)
                else:
                    attack_on(cla)
                    juljun_on(cla)
        else:
            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dungeon\\" + str(dun_cate) + "\\" + str(
                dun_name) + "\\" + "out_dun_in.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(25, 100, 215, 145, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dungeon out_dun_in", str(dun_name), imgs_)
                dun_in(cla, data)
            else:
                dun_in_ready(cla, data)
    except Exception as e:
        print(e)

def dun_in_ready(cla, data):
    print("dun_in_ready")

    # data = 던전_특수_버려진기지, 귀사당,, 별의낙원__4
    dun_data = data.split("_")
    dun_cate_ready = dun_data[1]
    dun_kind = dun_data[2]
    dun_step = dun_data[3]

    if dun_cate_ready == "특수":
        dun_cate = "special"
    elif dun_cate_ready == "파티":
        dun_cate = "party"
    if dun_kind == "버려진기지":
        dun_name = "giji"
    elif dun_kind == "귀사당":
        dun_name = "sadang"
    elif dun_kind == "별의낙원":
        dun_name = "star"
    elif dun_kind == "버려진광산":
        dun_name = "sab"
    elif dun_kind == "달빛사원":
        dun_name = "sawon"
    elif dun_kind == "제르비나의석상":
        dun_name = "jerbana"

    from potion import maul_potion
    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\dungeon.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(0, 30, 200, 200, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("title dungeon", imgs_)
    else:
        maul_potion(cla)

    complete = False

    is_ing = True
    is_ing_count = 0
    while is_ing is True:

        is_ing_count += 1

        if is_ing_count > 20:
            is_ing = False

        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\dungeon.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 200, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("title dungeon", imgs_)

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dungeon\\" + str(dun_cate) + "\\" + str(
                dun_name) + "\\" + "des_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(185, 320, 380, 380, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dungeon des_title", str(dun_name), imgs_)

                y_reg = (int(dun_step) * 50) + 305
                click_pos_2(100, y_reg, cla)

                QTest.qWait(500)

                click_pos_2(940, 720, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dungeon\\complete_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 80, 535, 145, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("complete_notice", imgs_)
                        myQuest_play_add(cla, data)
                        complete = True
                        is_ing = False
                        break
                    QTest.qWait(100)
                if complete == False:
                    # 들어갔는지 확인 후 공격!!
                    for i in range(10):
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dungeon\\" + str(dun_cate) + "\\" + str(
                            dun_name) + "\\" + "out_dun_in.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(25, 100, 215, 145, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("dungeon out_dun_in", str(dun_name), imgs_)
                            is_ing = False
                            dun_in(cla, data)
                            break
                        else:
                            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dungeon\\" + str(dun_cate) + "\\" + str(
                                dun_name) + "\\" + "des_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(185, 320, 380, 380, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("dungeon des_title", str(dun_name), imgs_)
                                click_pos_2(940, 720, cla)
                                time.sleep(1)
                        QTest.qWait(1000)


            else:

                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\clean_screen\\close\\close_6.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(955, 315, 1010, 360, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("close_6", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)

                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dungeon\\" + str(dun_cate) + "\\" + str(
                    dun_name) + "\\" + "kind.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 350, 1010, 450, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("dungeon kind", str(dun_name), imgs_)
                    x_reg = imgs_.x
                    y_reg = imgs_.y

                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dungeon\\befor_click_complete.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_reg, y_reg, x_reg + 100, 690, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("dungeon befor_click_complete", imgs_)
                        myQuest_play_add(cla, data)
                        complete = True
                        is_ing = False

                    else:
                        click_pos_reg(x_reg, 530, cla)

                else:

                    if dun_cate_ready == "특수":
                        click_pos_2(50, 95, cla)
                    elif dun_cate_ready == "파티":
                        click_pos_2(140, 95, cla)
                    QTest.qWait(500)








        else:

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\dungeon.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 30, 1010, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dungeon", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            else:
                menu_open(cla)
        QTest.qWait(1000)


def dun_in(cla, data):



    print("dun_in")

    # data = 던전_특수_버려진기지, 귀사당,, 별의낙원__4
    dun_data = data.split("_")
    dun_cate_ready = dun_data[1]
    dun_kind = dun_data[2]
    dun_step = dun_data[3]

    if dun_cate_ready == "특수":
        dun_cate = "special"
    elif dun_cate_ready == "파티":
        dun_cate = "party"
    if dun_kind == "버려진기지":
        dun_name = "giji"
    elif dun_kind == "귀사당":
        dun_name = "sadang"
    elif dun_kind == "별의낙원":
        dun_name = "star"
    elif dun_kind == "버려진광산":
        dun_name = "sab"
    elif dun_kind == "달빛사원":
        dun_name = "sawon"
    elif dun_kind == "제르비나의석상":
        dun_name = "jerbana"

    is_ing = True
    is_ing_count = 0
    while is_ing is True:

        is_ing_count += 1

        if is_ing_count > 20:
            is_ing = False

        result_juljun = juljun_check(cla)
        if result_juljun == True:

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dungeon\\" + str(dun_cate) + "\\" + str(
                dun_name) + "\\" + "juljun_dun_in.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(25, 100, 215, 145, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dungeon juljun_dun_in", str(dun_name), imgs_)

                is_ing = False

        else:
            # full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dungeon\\dun_in_map.PNG"
            # img_array = np.fromfile(full_path, np.uint8)
            # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            # imgs_ = imgs_set_(25, 100, 215, 145, cla, img, 0.8)
            # if imgs_ is not None and imgs_ != False:
            #     print("dungeon out_dun_in", str(dun_name), imgs_)

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dungeon\\" + str(dun_cate) + "\\" + str(
                dun_name) + "\\" + "out_dun_in.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(25, 100, 215, 145, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dungeon out_dun_in", str(dun_name), imgs_)
                go_random(cla)
                attack_on(cla)
                juljun_on(cla)

        QTest.qWait(1000)