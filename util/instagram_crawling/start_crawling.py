# -*- coding:utf-8 -*-

from get_data import crawling_instagram
from meta_data import *
from food_lists import item_lists
import time


def instagram_main(arguments):
    args = arguments

    is_file_save, is_tag_file_save = crawling_instagram(args=args)

    if is_file_save:
        print("file save success - {}_{}.csv".format(args["extract_file"], args["hash_tag"]))

    if is_tag_file_save:
        print("file save success - {}_{}.csv".format(args["extract_tag_file"], args["hash_tag"]))


if __name__ == "__main__":

    arguments = {
        "id": "",
        "password": "",
        "login_option": LOGIN_OPTION,
        "driver_path": DRIVER_PATH,
        "display": 1,
        "extract_file": SAVE_FILE_NAME,
        "extract_tag_file": SAVE_FILE_NAME_TAG,
        "hash_tag": "variable",
        "extract_num": EXTRACT_NUM,
    }

    for index, food in enumerate(item_lists):
        print("===== {}/{}번째 {} 음식 정보 크롤링 시작합니다. =====".format(index + 1, len(item_lists), food))

        arguments["hash_tag"] = food

        instagram_main(arguments)
        time.sleep(3)
