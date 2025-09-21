import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

from function_game import macro_out
import numpy as np
import cv2
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')


fix_list_ready = "c:\\my_games\\tsl\\data_tsl\\imgs\\check\\fix\\"
fix_list = os.listdir(fix_list_ready)

att_list_ready = "c:\\my_games\\tsl\\data_tsl\\imgs\\check\\attack\\"
att_list = os.listdir(att_list_ready)

jul_list_ready = "c:\\my_games\\tsl\\data_tsl\\imgs\\check\\juljun\\"
jul_list = os.listdir(jul_list_ready)

def out_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import imgs_set_
    from clean_screen import close_check

    try:
        print("out_check")

        is_out = False

        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\check\\out\\talk.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 800, 100, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("talk", imgs_)

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\character_select.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(740, 30, 1010, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("character_select", imgs_)
            else:
                result_close = close_check(cla)
                if result_close == False:
                    is_out = True

        return is_out

    except Exception as e:
        print(e)





def loading_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("loading_check")

        is_loding = False

        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\check\\loading\\loding_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(30, 680, 300, 900, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("loding_1", imgs_)
            is_loding = True

        return is_loding

    except Exception as e:
        print(e)


def loading_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("loading_check 30 680 300 900")

        is_loding = False
        is_loding_count = 0

        while is_loding is False:
            is_loding_count += 1
            if is_loding_count > 10:
                is_loding = True

            is_load = False

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\check\\loading\\loding_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 680, 300, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("loding_1", imgs_)
                is_load = True

            if is_load == True:
                QTest.qWait(1000)
            else:
                is_loding = True
            QTest.qWait(1000)



    except Exception as e:
        print(e)



def jangsigan_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open
    from massenger import line_to_me

    try:
        print("jangsigan_check")


        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\check\\longtime\\jangsigan.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 400, 600, 640, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("jangsigan", imgs_)
            line_to_me(cla, "장시간 미접속")

    except Exception as e:
        print(e)


def move_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("move_check")

        is_move = False

        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\check\\move\\move_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 530, 600, 800, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("move_2", imgs_)
            is_move = True
        else:
            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\jadong\\move_ing1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(210, 30, 1010, 1040, cla, img, 0.6)
            if imgs_ is not None and imgs_ != False:
                print("move_ing1", imgs_)
                is_move = True
            else:
                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\jadong\\move_ing2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(210, 30, 1010, 1040, cla, img, 0.6)
                if imgs_ is not None and imgs_ != False:
                    print("move_ing2", imgs_)
                    is_move = True

        return is_move


    except Exception as e:
        print(e)


def move_ing(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("move_ing")

        is_move = True
        is_move_count = 0
        while is_move is True:


            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\check\\move\\move_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(535, 680, 575, 705, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("move_2", imgs_)
                is_move = True
            else:
                is_move = False

            if is_move == False:
                is_move_count += 1
                if is_move_count < 6:
                    is_move = True

            QTest.qWait(200)

    except Exception as e:
        print(e)

def fix_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("fix_check")

        is_fix = False

        for i in range(len(fix_list)):

            full_path = str(fix_list_ready) + str(fix_list[i])
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 1010, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("fix_list", fix_list[i], imgs_)
                is_fix = True
                macro_out(cla)
                break
        return is_fix
    except Exception as e:
        print(e)


def attack_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import juljun_on

    try:
        print("attack_check")

        is_data = False
        is_data_count = 0
        while is_data is False:
            is_data_count += 1
            if is_data_count > 7:
                is_data = True



            result_jul = juljun_check(cla)
            if result_jul == True:

                is_data = True

                is_att = False
                for i in range(len(att_list)):

                    full_path = str(att_list_ready) + str(att_list[i])
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(440, 300, 580, 400, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("attack on", att_list[i], imgs_)
                        is_att = True
                        break
            else:
                juljun_on(cla)
            QTest.qWait(1000)




        return is_att
    except Exception as e:
        print(e)


def juljun_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("juljun_check")

        is_jul = False

        for i in range(len(jul_list)):

            full_path = str(jul_list_ready) + str(jul_list[i])
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 600, 600, 660, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("juljun on", jul_list[i], imgs_)
                is_jul = True
                break

        return is_jul
    except Exception as e:
        print(e)


def bag_open_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_

    try:
        print("bag_open_check")

        is_bag = False

        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\bag.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("title bag", imgs_)
            is_bag = True

        return is_bag
    except Exception as e:
        print(e)

