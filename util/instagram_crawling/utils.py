from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from pyvirtualdisplay import Display
import pandas as pd
import random
import time
import os
from meta_data import *


def delay_until_next_step(start, end):
    time.sleep(make_radom_sleep_time(start=start, end=end + 1))


def make_radom_sleep_time(start, end):
    return random.randrange(start=start, stop=end + 1)


def make_chrome_driver(driver_path, display_option):
    driver = None

    if display_option == 0:
        # display = Display(visible=0, size=(1920, 1080))
        # display.start()
        # options = wd.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('window-size=1920x1080')
        # options.add_argument("disable-gpu")
        # driver = wd.Chrome(driver_path, options=options)
        pass
    elif display_option == 1:
        driver = wd.Chrome(driver_path)

    return driver


def instagram_login(driver, user_id, user_password, login_option):
    is_login_success = False
    driver.get(LOGIN_URL)
    time.sleep(10)

    if login_option == "facebook":
        try:
            print("try click facebook login button 1")
            facebook_login_btn = driver.find_element_by_css_selector(FACEBOOK_LOGIN_PAGE_BTN_CSS_1)
            time.sleep(5)
            facebook_login_btn.click()
            is_facebook_btn_click = True
            is_login_success = True
        except:
            print("click facebook login button 1 fail")
            is_facebook_btn_click = False
            is_login_success = False

        time.sleep(10)

        if not is_facebook_btn_click:
            print("try click facebook login button 2")
            try:
                facebook_login_btn = driver.find_element_by_css_selector(FACEBOOK_LOGIN_PAGE_BTN_CSS_2)
                time.sleep(5)
                facebook_login_btn.click()
                is_facebook_btn_click = True
                is_login_success = True
            except:
                print("click facebook login button 2 fail")
                is_login_success = False

        time.sleep(10)

        if is_facebook_btn_click:
            id_input_form = driver.find_element_by_name(FACEBOOK_ID_FORM_NAME)
            time.sleep(5)
            id_input_form.send_keys(user_id)

            time.sleep(7)

            pw_input_form = driver.find_element_by_name(FACEBOOK_PW_FORM_NAME)
            time.sleep(5)
            pw_input_form.send_keys(user_password)

            time.sleep(7)

            login_btn = driver.find_element_by_name(FACEBOOK_LOGIN_BTN)
            time.sleep(5)
            login_btn.click()
        time.sleep(10)
    else:
        print("????????? ????????? ????????? ?????????.")

    return is_login_success


def move_hash_tag_page(driver, hash_tag):
    try:
        hash_tag_url = CONTENT_URL + hash_tag
        driver.get(hash_tag_url)
        time.sleep(10)
        is_move_success = True
    except:
        is_move_success = False

    return is_move_success


def click_first_image(driver):
    try:
        driver.find_element_by_css_selector(FIRST_IMG_CSS).click()
        is_first_img_click_success = True
    except:
        is_first_img_click_success = False

    return is_first_img_click_success


def click_next_arrow_button(driver):
    try:
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, NEXT_ARROW_BTN_CSS_1)))
        driver.find_element_by_css_selector(NEXT_ARROW_BTN_CSS_2).click()
        check_arrow = True
    except:
        check_arrow = False

    return check_arrow


def save_extract_data_to_csv_file(location_infos, location_hrefs, upload_ids, date_texts,
                                  date_times, date_titles, main_texts, save_file_name, hash_tag):
    try:
        insta_info_df = pd.DataFrame(
            {"location_info": location_infos, "location_href": location_hrefs, "upload_id": upload_ids,
             "date_text": date_texts, "date_time": date_times, "date_title": date_titles, "main_text": main_texts})
        if not os.path.exists('./results'):
            os.makedirs("./results")
        insta_info_df.to_csv("./results/{}_{}.csv".format(save_file_name, hash_tag),
                             encoding="utf-8-sig",
                             index=False)
        is_save_file_success = True
    except:
        is_save_file_success = False

    return is_save_file_success


def save_extract_tag_data_to_csv_file(instagram_tags, save_file_name_tag, hash_tag):
    try:
        insta_tag_df = pd.DataFrame({"tag": instagram_tags})

        if not os.path.exists('./results'):
            os.makedirs("./results")
        insta_tag_df.to_csv("./results/{}_{}.csv".format(save_file_name_tag, hash_tag),
                            encoding="utf-8-sig",
                            index=False)
        is_save_tag_file_success = True
    except:
        is_save_tag_file_success = False

    return is_save_tag_file_success
