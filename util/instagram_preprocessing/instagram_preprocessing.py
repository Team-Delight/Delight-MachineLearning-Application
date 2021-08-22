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
            if tag in ['Noun'] and (food_name not in word) and \
                    ("맛집" not in word) and ("추천" not in word) and ("맥도날드" not in word) and ("그램" not in word) and \
                    ("스타" not in word) and ("오늘" not in word) and ("맥날" not in word) and ("일상" not in word) and \
                    ("메뉴" not in word) and ("요리" not in word) and ("돈가스" not in word) and ("돈까스" not in word) and \
                    ("통모" not in word) and ("명랑" not in word) and ("핫도그" not in word) and ("세종" not in word) and \
                    ("맞팔" not in word) and ("까르보나라" not in word) and ("메루" not in word) and ("전포동" not in word) and \
                    ("호사" not in word) and ("나폴리" not in word) and ("누드" not in word) and ("김밥" not in word) and \
                    ("진짜" not in word) and ("단계" not in word) and ("생각" not in word) and ("애견" not in word) and \
                    ("더블" not in word) and ("레이더스" not in word) and ("데리" not in word) and ("사람" not in word) and \
                    ("텐동" not in word) and ("난파" not in word) and ("전문점" not in word) and ("사가정로" not in word) and \
                    ("중랑구" not in word) and ("면목동" not in word) and ("라멘" not in word) and ("지로" not in word) and \
                    ("돈코츠" not in word) and ("매운갈비찜" not in word) and ("푸드" not in word) and ("반야월" not in word) and \
                    ("유미" not in word) and ("카츠" not in word) and ("맛스타" not in word) and ("떡볶이" not in word) and \
                    ("할인" not in word) and ("마르" not in word) and ("팔공산" not in word) and ("리타" not in word) and \
                    ("마제" not in word) and ("다소" not in word) and ("먹방" not in word) and ("만두라" not in word) and \
                    ("라면" not in word) and ("카레돈가스" not in word) and ("카레" not in word) and ("명량" not in word) and \
                    ("모리" not in word) and ("버거킹" not in word) and ("몬스터" not in word) and ("와퍼" not in word) and \
                    ("햄버거" not in word) and ("새천년" not in word) and ("돈코츠" not in word) and ("마쯔리" not in word) and \
                    ("미소" not in word) and ("디럭스" not in word) and ("베토디" not in word) and ("혜택" not in word) and \
                    ("타르" not in word) and ("싸가지" not in word) and ("구매" not in word) and ("싸이" not in word) and \
                    ("터치" not in word) and ("맘스" not in word) and ("상하이어" not in word) and ("상하이" not in word) and \
                    ("선팔" not in word) and ("광주" not in word) and ("가스" not in word) and ("순두부찌개" not in word) and \
                    ("키트" not in word) and ("동탄" not in word) and ("대국" not in word) and ("충무로" not in word) and \
                    ("정식" not in word) and ("음식" not in word) and ("시오" not in word) and ("토리" not in word) and \
                    ("블랙" not in word) and ("퍼스트" not in word) and ("아메리칸" not in word) and ("야끼소바" not in word) and \
                    ("네기마" not in word) and ("성수동" not in word) and ("성수" not in word) and ("양장" not in word) and \
                    ("장마당" not in word) and ("공구" not in word) and ("연남" not in word) and ("트럴" not in word) and \
                    ("이요" not in word) and ("논현" not in word) and ("명촌" not in word) and ("마리" not in word) and \
                    ("맛스타" not in word) and ("라야" not in word) and ("노출" not in word) and ("게시" not in word) and \
                    ("팔로워" not in word) and ("문의" not in word) and ("계정" not in word) and ("오레" not in word) and \
                    ("콰트로" not in word) and ("와퍼" not in word) and ("기네스" not in word) and ("참여" not in word) and \
                    ("최고" not in word) and ("리조또" not in word) and ("스푼" not in word) and ("트러플" not in word) and \
                    ("머쉬룸" not in word) and ("피어싱" not in word) and ("피맥" not in word) and ("플레이" not in word) and \
                    ("볶이" not in word) and ("짬뽕" not in word) and ("함덕" not in word) and ("애월" not in word) and \
                    ("청주" not in word) and ("화이트" not in word) and ("서구청" not in word) and \
                    ("맛" not in word) and ("맥" not in word) and ("글" not in word) and ("모" not in word) and \
                    ("식" not in word) and ("불" not in word) and ("군" not in word) and ("만" not in word) and \
                    ("쇼" not in word) and ("핫" not in word) and ("메" not in word) and ("베" not in word) and \
                    ("살" not in word) and ("개" not in word) and ("낚" not in word) and ("냉" not in word) and \
                    ("회심" not in word) and ("말" not in word) and ("비스트" not in word) and ("더" not in word) and \
                    ("세트" not in word) and ("트" not in word) and ("소통" not in word) and ("점" not in word) and \
                    ("리" not in word) and ("층" not in word) and ("것" not in word) and ("수" not in word) and \
                    ("갈비찜" not in word) and ("경산" not in word) and ("피" not in word) and ("제리" not in word) and \
                    ("아라르" not in word) and ("칸" not in word) and ("부" not in word) and ("곳" not in word) and \
                    ("내" not in word) and ("베" not in word) and ("듬" not in word) and ("통" not in word) and \
                    ("이프" not in word) and ("를" not in word) and ("점" not in word) and ("살" not in word) and \
                    ("월" not in word) and ("트" not in word) and ("차" not in word) and ("토" not in word) and \
                    ("구독" not in word) and ("맥" not in word) and ("슈" not in word) and ("글" not in word) and \
                    ("환영" not in word) and ("느낌" not in word) and ("것" not in word) and ("준" not in word) and \
                    ("안" not in word) and ("때" not in word) and ("리오" not in word) and ("곳" not in word) and \
                    ("뎅" not in word) and ("함유" not in word) and ("산" not in word) and ("만" not in word) and \
                    ("인기" not in word) and ("스" not in word) and ("활동" not in word) and ("프로필" not in word) and \
                    ("만큼" not in word) and ("노" not in word) and ("어간" not in word) and ("램" not in word) and \
                    ("이번" not in word) and ("행사" not in word) and ("최강" not in word) and ("이벤트" not in word) and \
                    ("주" not in word) and ("홈쿡" not in word) and ("팅" not in word) and ("로" not in word) and \
                    ("맵" not in word) and ("줄" not in word) and ("이" not in word) and ("날" not in word) and \
                    ("오픈" not in word) and ("요" not in word) and ("데" not in word) and ("인" not in word) and \
                    ("저" not in word) and ("함" not in word) and ("톳" not in word) and ("무난" not in word) and \
                    ("끼" not in word) and ("감" not in word) and ("쉬" not in word) and ("또" not in word) and \
                    ("헤" not in word) and ("달랏" not in word) and ("디어" not in word) and ("나" not in word) and \
                    ("디" not in word) and ("화" not in word) and ("중" not in word) and ("일" not in word) and \
                    ("맘터" not in word) and ("링크" not in word) and ("또" not in word) and ("콜린" not in word) and \
                    ("거" not in word) and ("도" not in word) and ("날" not in word) and ("꼭" not in word) and \
                    ("세" not in word) and ("마카" not in word) and ("츠" not in word) and ("뉴저지" not in word) and \
                    ("세상" not in word) and ("충" not in word) and ("방" not in word) and ("끼" not in word) and \
                    ("그레이" not in word) and ("종" not in word) and ("나" not in word) and ("쥬" not in word) and \
                    ("이" not in word) and ("컵" not in word) and ("도" not in word) and ("코" not in word) and \
                    ("찾기" not in word) and ("단" not in word) and ("시" not in word) and ("날" not in word):
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

    for idx, food_csv in enumerate(extract_csv_lists):
        food_name = food_csv.split("_")[2].split(".")[0]
        food = pd.read_csv(os.path.join(data_path, food_csv))
        total_text_list = sum_main_text(food)
        list_word = words_count(food_name, total_text_list)
        final_list_words = list_word[:10]

        food_dataframe = make_dataframe(food_name, final_list_words)
        instagram_data = pd.concat([instagram_data, food_dataframe])
        print("{}/{} {}은 전처리가 완료되었습니다.".format(idx + 1, len(extract_csv_lists), food_name))

    instagram_data.reset_index(drop=True, inplace=True)

    save_preprocessing_data(instagram_data)

    return instagram_data


if __name__ == "__main__":
    # Test
    RAWDATA_PATH = "../instagram_crawling/results/"

    print(start_preprocessing_all_foods(RAWDATA_PATH))
