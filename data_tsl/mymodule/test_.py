import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

kind_point_ready = "c:\\my_games\\tsl\\data_tsl\\imgs\\point\\"

def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import imgs_set_, click_pos_2, click_pos_reg, drag_pos, text_check_get_num

    from massenger import line_to_me
    from character_select_and_game_start import character_change, game_ready, game_start_screen
    from clean_screen import all_skip, close_check
    from get_item import get_post, get_event, get_upjuk, get_sangjum
    from check import attack_check, move_check
    from action import juljun_on, juljun_off, attack_on, go_maul, menu_open
    from potion import maul_potion,potion_check, potion_check_test
    from boonhae_collection import boonhae_setting, boonhae_collection_start, boonhae_start
    from dead import dead_die
    from clean_screen import skip_check
    from boonhae_collection import collection_start

    cla = "one"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    try:

        print("test")

        get_event(cla, "event")
        # point_ready = kind_point_ready + "event\\eight\\"
        # point_ = os.listdir(point_ready)
        # for p in range(len(point_)):
        #
        #     full_path = str(point_ready) + point_[p]
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(555, 500, 600, 700, cla, img, 0.8)
        #     if imgs_ is not None and imgs_ != False:
        #         print("event eight point", point_[p], imgs_)
        #         click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
        #         QTest.qWait(500)
        #         click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
        #     else:
        #
        #         full_path = str(point_ready) + point_[p]
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(800, 500, 850, 700, cla, img, 0.8)
        #         if imgs_ is not None and imgs_ != False:
        #             print("event eight point", point_[p], imgs_)
        #             click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
        #             QTest.qWait(500)
        #             click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\mission\\bosang_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(860, 960, 1010, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("bosang_btn", imgs_)

        # boonhae_start(cla)



    except Exception as e:
        print(e)

