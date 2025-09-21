
import sys
import os
import time

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

kind_num_ready = "c:\\my_games\\tsl\\data_tsl\\imgs\\potion\\num\\"
kind_num = os.listdir(kind_num_ready)

def potion_check(cla):
    import numpy as np
    import cv2

    from check import juljun_check, out_check
    from function_game import imgs_set_
    try:
        print("potion_check")

        is_potion = False

        result_juljun = juljun_check(cla)
        if result_juljun == True:
            # result = text_check_get_num(443, 1002, 451, 1018, cla)
            # print("result", result)

            for n in range(len(kind_num)):
                full_path = str(kind_num_ready) + str(kind_num[n])
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(443, 1002, 451, 1018, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("kind_num", str(kind_num[n]), imgs_)
                    result_num = kind_num[n].split("_")[0]
                    print("result_num", result_num)
                    is_potion = True
                    break
        else:
            result_out = out_check(cla)
            if result_out == True:
                # result = text_check_get_num(363, 1010, 373, 1023, cla)
                # print("result", result)

                for n in range(len(kind_num)):
                    full_path = str(kind_num_ready) + str(kind_num[n])
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(363, 1010, 373, 1023, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("kind_num", str(kind_num[n]), imgs_)
                        result_num = kind_num[n].split("_")[0]
                        print("result_num", result_num)
                        is_potion = True
                        break
        if is_potion == False:
            v_.potion_count += 1
            if v_.potion_count > 1:
                maul_potion(cla)

    except Exception as e:
        print(e)


def maul_potion(cla):
    import numpy as np
    import cv2

    from check import juljun_check, out_check, move_check, move_ing
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import go_maul
    from boonhae_collection import boonhae_collection_start
    try:
        print("maul_potion")


        is_potion = False
        is_potion_count = 0
        while is_potion is False:
            is_potion_count += 1
            if is_potion_count > 7:
                is_potion = True

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\jabhwa.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("title jabhwa", imgs_)
                click_pos_2(810, 1010, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\potion\\anymore_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 80, 700, 150, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("anymore_1", imgs_)
                        is_potion = True
                        break
                    QTest.qWait(100)
                if is_potion == False:
                    click_pos_2(940, 1010, cla)



            else:
                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\potion\\jabhwa_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(870, 970, 930, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("jabhwa_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(5):
                        result_move = move_check(cla)
                        if result_move == True:
                            move_ing(cla)
                            break
                        QTest.qWait(200)


                else:
                    go_maul(cla)

            QTest.qWait(200)
        for i in range(5):
            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\jabhwa.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(980, 55, cla)
            else:
                boonhae_collection_start(cla)
                break
            QTest.qWait(500)

    except Exception as e:
        print(e)
