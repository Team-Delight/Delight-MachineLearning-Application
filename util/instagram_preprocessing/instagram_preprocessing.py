import os
from collections import Counter

import pandas as pd
from konlpy.tag import Twitter


def extract_foods_name_and_csv_list(data_path):
    csv_lists = os.listdir(data_path)
    extract_csv_lists = [csv for csv in csv_lists if csv.split('_')[1] == "extract"]
    return extract_csv_lists


def sum_main_text(food):
    total_text_list = []
    for text in food["main_text"]:
        if type(text) == str:
            remove_hash_text = text.replace("#", " ")
            total_text_list.append(remove_hash_text)
        else:
            break
    return total_text_list


def words_count(food_name, text_list):
    instagram = Twitter()
    morphs = []

    for sentence in text_list:
        morphs.append(instagram.pos(sentence))

    noun_adj_adv_list = []
    for sentence in morphs:
        for word, tag in sentence:
            if tag in ['Noun'] and (len(word) != 1) and (food_name not in word) and \
                    ("맛집" not in word) and ("추천" not in word):
                noun_adj_adv_list.append(word)

    count = Counter(noun_adj_adv_list)
    list_words = list(count.most_common())
    return list_words


def make_dataframe(food_name, final_list_words):
    lists = []
    for i in final_list_words:
        lists.append(i[0])
    lists.insert(0, food_name)

    record = pd.DataFrame(lists).transpose()
    record.columns = ['title'] + ["feature" + str(num) for num in range(1, 11)]

    return record


def save_preprocessing_data(instagram_data):
    if not os.path.exists('./results'):
        os.makedirs("./results")

    instagram_data.to_csv("./results/instagram_food_data.csv",
                          encoding="utf-8-sig",
                          index=False)


def start_preprocessing_all_foods(data_path):
    extract_csv_lists = extract_foods_name_and_csv_list(data_path)

    instagram_data = pd.DataFrame(columns=['title'] + ["feature" + str(num) for num in range(1, 11)])

    for food_csv in extract_csv_lists:
        food_name = food_csv.split("_")[2].split(".")[0]
        food = pd.read_csv(os.path.join(data_path, food_csv))
        total_text_list = sum_main_text(food)
        list_word = words_count(food_name, total_text_list)
        final_list_words = list_word[:10]

        food_dataframe = make_dataframe(food_name, final_list_words)
        instagram_data = pd.concat([instagram_data, food_dataframe])

    instagram_data.reset_index(drop=True, inplace=True)

    save_preprocessing_data(instagram_data)

    return instagram_data


if __name__ == "__main__":
    rawdata_path = "../instagram_crawling/results/"

    print(start_preprocessing_all_foods(rawdata_path))
