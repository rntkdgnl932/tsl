import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_
from check import out_check
import numpy as np
import cv2
from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos, change_number
from clean_screen import clean_screen_start, close_check
from check import juljun_check, attack_check



sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

kind_confirm = "c:\\my_games\\tsl\\data_tsl\\imgs\\action\\confirm_all"
kind_confirm_list = os.listdir(kind_confirm)

def menu_open(cla):

    try:
        print("menu_open")

        is_action = False
        is_action_count = 0

        while is_action is False:
            is_action_count += 1
            if is_action_count > 5:
                is_action = True



            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\character_select.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(740, 30, 1010, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("character_select", imgs_)

                result_close = close_check(cla)
                if result_close == False:
                    is_action = True
            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(975, 55, cla)
                else:
                    clean_screen_start(cla)
            QTest.qWait(100)

    except Exception as e:
        print(e)


def confirm_all(cla):


    try:
        print("confirm_all")

        is_action = False
        is_action_count = 0

        is_confirm = False

        while is_action is False:
            is_action_count += 1
            if is_action_count > 3:
                is_action = True



            for i in range(len(kind_confirm_list)):

                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\action\\confirm_all\\" + str(kind_confirm_list[i])
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 1010, 990, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("confirm_1", str(kind_confirm_list[i]), imgs_)
                    is_confirm = True
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\action\\confirm_all\\" + str(kind_confirm_list[i])
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 650, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("confirm_1", str(kind_confirm_list[i]), imgs_)
                        is_confirm = True
                        click_pos_reg(imgs_.x, imgs_.y, cla)

            if is_confirm == True:
                is_confirm = False
                QTest.qWait(1000)
            else:
                is_action = True
            QTest.qWait(100)
        return is_confirm
    except Exception as e:
        print(e)


def cancle_all(cla):
    print("cancle_all")




def juljun_on(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_

    try:
        print("juljun_on")

        is_jul = False
        is_jul_count = 0
        while is_jul is False:
            is_jul_count += 1
            if is_jul_count > 7:
                is_jul = True


            result_jul = juljun_check(cla)
            if result_jul == True:
                is_jul = True
            else:
                clean_screen_start(cla)
                click_pos_2(20, 925, cla)
            QTest.qWait(1000)



    except Exception as e:
        print(e)

def juljun_off(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_

    try:
        print("juljun_off")

        is_jul = False
        is_jul_count = 0
        while is_jul is False:
            is_jul_count += 1
            if is_jul_count > 7:
                is_jul = True

            result_jul = juljun_check(cla)
            if result_jul == True:
                drag_pos(440, 490, 800, 490, cla)
                QTest.qWait(1000)
            else:
                result_out = out_check(cla)
                if result_out == True:
                    is_jul = True
                else:
                    clean_screen_start(cla)
            QTest.qWait(1000)

    except Exception as e:
        print(e)


def attack_on(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_

    try:
        print("attack_on")

        is_att = False
        is_att_count = 0
        while is_att is False:
            is_att_count += 1
            if is_att_count > 7:
                is_att = True


            result_att = attack_check(cla)
            if result_att == True:
                is_att = True
            else:
                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\action\\attack\\auto_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(940, 850, 1010, 910, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("auto_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(300)
                    click_pos_2(20, 925, cla)
                else:
                    result_out = out_check(cla)
                    if result_out == True:
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\action\\attack\\auto_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(940, 850, 1010, 910, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("auto_btn", imgs_)
                            click_pos_2(980, 880, cla)
                            QTest.qWait(300)
                            click_pos_2(20, 925, cla)

                    else:
                        clean_screen_start(cla)
                        click_pos_2(980, 880, cla)
                        QTest.qWait(300)
                        click_pos_2(20, 925, cla)
            QTest.qWait(1000)



    except Exception as e:
        print(e)


def go_maul(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_

    try:
        print("go_maul")

        is_ = False
        is_count = 0
        while is_ is False:
            is_count += 1
            if is_count > 7:
                is_ = True

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\potion\\jabhwa_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(870, 970, 930, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("jabhwa_btn", imgs_)
                is_ = True
            else:
                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\action\\go_maul\\maul_teleport.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(565, 975, 625, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("maul_teleport", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(3000)
                else:
                    clean_screen_start(cla)

            QTest.qWait(1000)



    except Exception as e:
        print(e)


def bag_open(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_
    from check import bag_open_check

    try:
        print("bag_open")

        is_ = False
        is_count = 0
        while is_ is False:
            is_count += 1
            if is_count > 7:
                is_ = True

            result_bag = bag_open_check(cla)
            if result_bag == True:
                is_ = True

                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\action\\bag_open\\jadong_jangchak_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(880, 990, 1010, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("jadong_jangchak_btn collection", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

            else:
                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\bag_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 30, 1010, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("bag_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\bag_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 30, 1010, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("bag_2", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        clean_screen_start(cla)




            QTest.qWait(1000)



    except Exception as e:
        print(e)













