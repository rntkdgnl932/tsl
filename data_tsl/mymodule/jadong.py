import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def jadong_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from check import attack_check
    from potion import potion_check


    try:

        print("jadong_start")

        result_attack = attack_check(cla)
        if result_attack == True:
            potion_check(cla)
        else:
            go_spot(cla)



    except Exception as e:
        print(e)


def go_spot(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import imgs_set_, click_pos_2, click_pos_reg, imgs_set_for

    from massenger import line_to_me
    from character_select_and_game_start import character_change, game_ready, game_start_screen
    from clean_screen import clean_screen_start
    from get_item import get_post, get_event, get_upjuk
    from check import attack_check, out_check, move_check, move_ing
    from action import juljun_on, juljun_off, attack_on
    from potion import potion_check


    try:

        print("go_spot")

        is_data = False
        is_data_count = 0
        while is_data is False:
            is_data_count += 1
            if is_data_count > 10:
                is_data = True


            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\jadong\\move.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 600, 610, 640, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("move", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                is_data = True

                for i in range(10):
                    result_move = move_check(cla)
                    if result_move == True:
                        break
                    QTest.qWait(200)
                for i in range(5):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\jadong\\like_spot_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 30, 160, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("like_spot_title", imgs_)
                        click_pos_2(985, 55, cla)
                    else:
                        break
                    QTest.qWait(500)

                for i in range(10):
                    result_move = move_check(cla)
                    if result_move == True:
                        move_ing(cla)
                        attack_on(cla)
                        juljun_on(cla)
                        break

                    QTest.qWait(200)



            else:

                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\jadong\\82_move.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(840, 980, 1010, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("like_spot_title", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:

                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\jadong\\like_spot_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 30, 160, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("like_spot_title", imgs_)
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\jadong\\spot_list.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_for = imgs_set_for(35, 75, 90, 500, cla, img, 0.8)
                        if imgs_for is not None and imgs_for != False:
                            if len(imgs_for) > 0:
                                random_spot = random.randint(0, len(imgs_for))
                                y_reg = imgs_for[random_spot][1]
                                click_pos_reg(110, y_reg, cla)



                    else:
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\jadong\\like_spot_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 195, 50, 250, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("like_spot_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:

                            result_out = out_check(cla)
                            if result_out == True:
                                click_pos_2(110, 180, cla)
                            else:
                                clean_screen_start(cla)

            QTest.qWait(1000)




    except Exception as e:
        print(e)