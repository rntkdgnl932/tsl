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


def dungeon_start(cla, data):
    try:
        print("dungeon_start")
        dun_in(cla, data)
    except Exception as e:
        print(e)

def dun_in(cla, data):
    print("dun_in")

    # data = 던전_특수_버려진기지, 귀사당,, 별의낙원__4
    dun_data = data.split("_")
    dun_cate_ready = dun_data[1]
    dun_kind = dun_data[2]
    dun_step = dun_data[3]

    if dun_cate_ready == "특수":
        dun_cate = "specail"
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

        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\dungeon.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 200, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("title dungeon", imgs_)

            if dun_cate_ready == "특수":
                click_pos_2(50, 95, cla)
                QTest.qWait(500)
            elif dun_cate_ready == "파티":
                click_pos_2(140, 95, cla)
                QTest.qWait(500)

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\dungeon\\" + str(dun_cate) + "\\" + str(dun_name) + "\\" + "kind.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 350, 1010, 450, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("kind dungeon", str(dun_name), imgs_)
                click_pos_reg(imgs_.x, 530, cla)




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

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\dungeon.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 30, 1010, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dungeon", imgs_)
                x_ = imgs_.x
                y_ = imgs_.y
                click_pos_reg(x_, y_, cla)

            else:
                menu_open(cla)
        QTest.qWait(1000)