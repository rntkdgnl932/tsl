import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import imgs_set_, click_pos_2, click_pos_reg, drag_pos, text_check_get_num

    from massenger import line_to_me
    from character_select_and_game_start import character_change, game_ready, game_start_screen
    from clean_screen import all_skip
    from get_item import get_post, get_event, get_upjuk
    from check import attack_check, move_check
    from action import juljun_on, juljun_off, attack_on, go_maul
    from potion import maul_potion,potion_check
    from boonhae_collection import boonhae_setting, boonhae_collection_start, boonhae_start
    from dead import dead_die
    from clean_screen import skip_check
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

        get_event(cla)
        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\mission\\bosang_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(860, 960, 1010, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("bosang_btn", imgs_)

        # boonhae_start(cla)



    except Exception as e:
        print(e)

