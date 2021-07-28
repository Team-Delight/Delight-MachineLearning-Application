# -*- coding:utf-8 -*-

import argparse
from meta_data import *
from get_data import crawling_instagram


parser = argparse.ArgumentParser(description='Crawling Instagram Post',
                                 formatter_class=argparse.RawTextHelpFormatter)


def get_arguments():

    parser.add_argument("--id",
                        help="instagram or facebook id",
                        required=True, type=str)

    parser.add_argument("--password",
                        help="instagram or facebook password",
                        required=True, type=str)

    parser.add_argument("--hash_tag",
                        help="The hashtag you want to extract.",
                        default=HASH_TAG, type=str)

    parser.add_argument("--display",
                        help="display selenium chromedriver or not 0 or 1",
                        default=1, type=int)

    parser.add_argument("--driver_path",
                        help="selenium chrome driver path",
                        default=DRIVER_PATH, type=str)

    parser.add_argument("--extract_num",
                        help="The number of posts I want to extract.",
                        default=EXTRACT_NUM, type=int)

    parser.add_argument("--login_option",
                        help="select login account [facebook, instagram]",
                        default=LOGIN_OPTION, type=str)

    parser.add_argument("--extract_file",
                        help="set extract file name",
                        default=SAVE_FILE_NAME, type=str)

    parser.add_argument("--extract_tag_file",
                        help="set extract tag file name",
                        default=SAVE_FILE_NAME_TAG, type=str)

    _args = parser.parse_args()

    return _args


def instagram_main():
    args = get_arguments()
    is_file_save, is_tag_file_save = crawling_instagram(args=args)

    if is_file_save:
        print("file save success - {}_{}.csv".format(args.extract_file, HASH_TAG))

    if is_tag_file_save:
        print("file save success - {}_{}.csv".format(args.extract_tag_file, HASH_TAG))


if __name__ == "__main__":
    instagram_main()