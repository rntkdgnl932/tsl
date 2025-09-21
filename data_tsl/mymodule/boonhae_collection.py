import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

kind_point_ready = "c:\\my_games\\tsl\\data_tsl\\imgs\\point\\"

def boonhae_collection_start(cla):
    from action import bag_open
    from check import bag_open_check
    try:
        print("boonhae_collection_start")
        # 콜렉전 장비 체크(자동장착)
        bag_open(cla)

        collection_start(cla)

        boonhae_start(cla)
    except Exception as e:
        print(e)


def collection_start(cla):
    import numpy as np
    import cv2

    from check import juljun_check, out_check, move_check, move_ing
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import go_maul, menu_open
    try:
        print("collection_start")


        is_bc = False
        is_bc_count = 0
        while is_bc is False:
            is_bc_count += 1
            if is_bc_count > 10:
                is_bc = True

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("title collection", imgs_)

                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\item_collection_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 400, 600, 500, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("item_collection_title", imgs_)
                    click_pos_2(530, 580, cla)
                    QTest.qWait(500)
                    click_pos_2(530, 615, cla)
                    QTest.qWait(500)


                is_point = False
                point_ready = kind_point_ready + "collection\\top\\"
                point_ = os.listdir(point_ready)
                for p in range(len(point_)):
                    full_path = str(point_ready) + point_[p]
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(40, 65, 500, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("collection top point!!!!!", point_[p], imgs_)
                        is_point = True
                        click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                        QTest.qWait(500)
                        break
                if is_point == True:
                    point_ready = kind_point_ready + "collection\\item\\"
                    point_ = os.listdir(point_ready)
                    for p in range(len(point_)):
                        full_path = str(point_ready) + point_[p]
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 120, 600, 990, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("collection item point!!!!!", point_[p], imgs_)
                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                            QTest.qWait(500)
                            click_pos_2(900, 945, cla)
                            QTest.qWait(500)
                            if is_bc_count > 0:
                                is_bc_count -= 1
                            break
                else:
                    is_bc = True



            else:
                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\menu\\collection.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 30, 1010, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("collection", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(5):
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\collection.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        QTest.qWait(200)


                else:
                    menu_open(cla)

            QTest.qWait(200)
        for i in range(5):
            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(980, 55, cla)
            else:
                break
            QTest.qWait(500)

    except Exception as e:
        print(e)


def boonhae_start(cla):
    import numpy as np
    import cv2

    from check import juljun_check, out_check, move_check, move_ing
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import bag_open, menu_open
    from check import bag_open_check
    try:
        print("boonhae_start")


        is_bc = False
        is_bc_count = 0
        while is_bc is False:
            is_bc_count += 1
            if is_bc_count > 10:
                is_bc = True

            result_bag = bag_open_check(cla)
            if result_bag == True:
                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\boonhae_setting_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 960, 880, 995, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("title boonhae_setting_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)
                    boonhae_setting(cla)
                    QTest.qWait(500)
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\boonhae_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 990, 880, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("boonhae_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                else:
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\action\\bag_open\\bilhwal_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 990, 880, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("title ilhwal_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

            else:
                bag_open(cla)



            QTest.qWait(200)
        for i in range(5):
            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\title\\collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(980, 55, cla)
            else:
                break
            QTest.qWait(500)

    except Exception as e:
        print(e)


def boonhae_setting(cla):
    import numpy as np
    import cv2

    from check import juljun_check, out_check, move_check, move_ing
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import bag_open, menu_open
    from check import bag_open_check
    try:
        print("boonhae_setting")

        is_bc = False
        is_bc_count = 0
        while is_bc is False:
            is_bc_count += 1
            if is_bc_count > 10:
                is_bc = True

            success = False

            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\boonhae_setting_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(450, 380, 550, 420, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("title boonhae_setting_title", imgs_)

                # 일반
                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\checked_common.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(380, 520, 430, 560, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("일반 checked_common", imgs_)

                    # 고급
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(490, 520, 540, 560, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("고급 checked", imgs_)

                        # 수집
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 605, 420, 645, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("수집 checked", imgs_)

                            # 나머지 해제되어 있어야 성공

                            full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(380, 430, 420, 475, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("강화 해제 해야함", imgs_)

                            else:
                                full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(610, 515, 655, 560, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("희귀 해제 해야함", imgs_)
                                else:
                                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(380, 545, 420, 580, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("영웅 해제 해야함", imgs_)
                                    else:
                                        success = True

            if success == True:
                is_bc = True

                for i in range(5):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\boonhae_setting_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(450, 380, 550, 420, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("title boonhae_setting_title", imgs_)

                        click_pos_2(560, 670, cla)
                    else:
                        break
                    QTest.qWait(500)
            else:
                ##############################################
                print("일반체크")
                for i in range(4):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\checked_common.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 520, 430, 560, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("일반 checked_common", imgs_)
                        break
                    else:
                        click_pos_2(430, 535, cla)
                    QTest.qWait(500)


                print("고급체크")
                for i in range(4):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(490, 520, 540, 560, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("고급 checked", imgs_)
                        break
                    else:
                        full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\not_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(490, 520, 540, 560, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("고급 not_checked", imgs_)
                            click_pos_2(545, 535, cla)
                    QTest.qWait(500)

                print("수집체크")
                for i in range(4):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 605, 420, 645, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("수집 checked", imgs_)
                        break
                    else:
                        click_pos_2(430, 625, cla)
                    QTest.qWait(500)
                ##############################################
                print("나머지 해제하기")
                print("강화 해제")
                for i in range(5):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 430, 420, 475, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("강화 해제 checked", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)
                print("희귀 해제")
                for i in range(5):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(610, 515, 655, 560, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("희귀 해제 checked", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)
                print("영웅 해제")
                for i in range(5):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 545, 600, 580, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("영웅 해제 checked", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)

                print("영웅 해제")
                for i in range(5):
                    full_path = "c:\\my_games\\tsl\\data_tsl\\imgs\\boonhae_collection\\checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 545, 420, 580, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("영웅 해제 checked", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)



            QTest.qWait(500)

    except Exception as e:
        print(e)







