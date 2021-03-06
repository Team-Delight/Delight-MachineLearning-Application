# -*- coding:utf-8 -*-

import re

from utils import *


def get_location_data(driver):
    try:
        location_object = driver.find_element_by_css_selector(LOCATION_CSS)
        location_info = location_object.text
        location_href = location_object.get_attribute("href")
    except:
        location_info = None
        location_href = None

    return location_info, location_href


def get_upload_user_id(driver):
    try:
        upload_id_object = driver.find_element_by_css_selector(UPLOAD_USER_ID_CSS)
        upload_id = upload_id_object.text
    except:
        upload_id = None

    return upload_id


def get_date_info(driver):
    try:
        date_object = driver.find_element_by_css_selector(DATE_CSS)
        date_text = date_object.text
        date_time = date_object.get_attribute("datetime")
        date_title = date_object.get_attribute("title")
    except:
        date_text = None
        date_time = None
        date_title = None

    return date_text, date_time, date_title


def get_main_text(driver, instagram_tags):
    try:
        main_text_object = driver.find_element_by_css_selector(MAIN_TEXT_CSS)
        main_text = main_text_object.text
    except:
        main_text = None

    try:
        data = driver.find_element_by_css_selector(HASH_TAG_CSS)
        tag_raw = data.text
        tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
        tag = ''.join(tags).replace("#", " ")

        tag_data = tag.split()

        for tag_one in tag_data:
            instagram_tags.append(tag_one)
    except:
        pass

    return main_text, instagram_tags


def crawling_instagram(args):
    location_infos, location_hrefs = [], []
    date_texts, date_times, date_titles = [], [], []
    upload_ids, main_texts, instagram_tags = [], [], []

    user_id, user_password = args["id"], args["password"]
    login_option = args["login_option"]
    driver_path, display_option = args["driver_path"], args["display"]
    save_file_name, save_tag_file_name = args["extract_file"], args["extract_tag_file"]

    is_login_success, is_move_success, is_first_img_click_success = False, False, False

    driver = make_chrome_driver(driver_path=driver_path, display_option=display_option)

    if driver is not None:
        is_login_success = instagram_login(driver=driver, user_id=user_id, user_password=user_password,
                                           login_option=login_option)
    if is_login_success:
        hash_tag = args["hash_tag"]
        is_move_suceess = move_hash_tag_page(driver=driver, hash_tag=hash_tag)

    if is_move_suceess:
        is_first_img_click_success = click_first_image(driver=driver)

    if is_first_img_click_success:
        check_arrow = True
        count_extract_num = 0
        wish_num = args["extract_num"]

        while True:
            if count_extract_num > wish_num or not check_arrow:
                break

            delay_until_next_step(start=5, end=8)

            location_info, location_href = get_location_data(driver=driver)

            upload_user_id = get_upload_user_id(driver=driver)

            date_text, date_time, date_title = get_date_info(driver=driver)

            main_text, instagram_tags = get_main_text(driver=driver, instagram_tags=instagram_tags)

            count_extract_num += 1

            location_infos.append(location_info)
            location_hrefs.append(location_href)
            upload_ids.append(upload_user_id)
            date_texts.append(date_text)
            date_times.append(date_time)
            date_titles.append(date_title)
            main_texts.append(main_text)

            delay_until_next_step(start=5, end=7)

            check_arrow = click_next_arrow_button(driver=driver)

        is_save_file_success = save_extract_data_to_csv_file(location_infos=location_infos,
                                                             location_hrefs=location_hrefs,
                                                             upload_ids=upload_ids, date_texts=date_texts,
                                                             date_times=date_times, date_titles=date_titles,
                                                             main_texts=main_texts, save_file_name=save_file_name,
                                                             hash_tag=hash_tag)
        is_save_tag_file_success = save_extract_tag_data_to_csv_file(instagram_tags=instagram_tags,
                                                                     save_file_name_tag=save_tag_file_name,
                                                                     hash_tag=hash_tag)
    driver.close()
    driver.quit()

    return is_save_file_success, is_save_tag_file_success
