import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_ROOT = "./util/instagram_preprocessing/results/input_data.csv"

def custom_array(title, similarity):
    return {arg[0]: arg[1][1] for arg in zip(title, similarity)}


def make_input_data(data_path):
    food_info = pd.read_csv(data_path, encoding="utf-8")
    food_info['soup'] = food_info.apply(create_soup, axis=1)
    return food_info


def create_soup(food_info):
    ing = food_info['ingredients'].replace(",", "").replace("[", "").replace("]", "").replace("'", "")
    insta = food_info['instagram'].replace(",", "").replace("[", "").replace("]", "").replace("'", "")
    return ing + insta


def make_count_vectorizer(series):
    count = CountVectorizer()
    count_matrix = count.fit_transform(series)
    return count_matrix


def get_recommendations(title, indices, cosine_sim, dataframe):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return dataframe['title'].iloc[movie_indices], sim_scores


def one_food_collaborative_filtering(title, data_path):
    food_info = make_input_data(data_path)
    count_matrix = make_count_vectorizer(food_info['soup'])

    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    indices = pd.Series(food_info.index, index=food_info['title'])

    results, sim_scores = get_recommendations(title, indices, cosine_sim, food_info)
    return results.tolist(), sim_scores

def percentage_score(score_list):
    percentage = list(map(lambda x: (x / sum(score_list)) * 100, score_list))
    result = list(map(lambda x: round(x, 1), percentage))
    result[2] = round(100.0 - (result[0] + result[1]), 1)
    return result


def foods_collaborative_filtering(foods_list, data_path):
    final_result = dict()
    foods_name_list = set()

    for food in foods_list:
        recommendations, score = one_food_collaborative_filtering(food, data_path)

        consideration_food = custom_array(recommendations, score)
        new_food_name_list = set(consideration_food) - foods_name_list
        duplicated_foods_list = set(consideration_food) - new_food_name_list

        for food in recommendations:
            if food not in foods_list:
                if food in new_food_name_list:
                    final_result[food] = consideration_food[food]
                    foods_name_list.add(food)
                if food in duplicated_foods_list:
                    final_result[food] += consideration_food[food]

    food_top3 = sorted(final_result.items(), key=(lambda x: x[1]), reverse=True)[:3]
    food_top3_list = [food[0] for food in food_top3]
    food_top3_score = percentage_score([food[1] for food in food_top3])
    return food_top3_list, food_top3_score


if __name__ == "__main__":
    # Test
    foods_list = ['해물쟁반짜장', '사천짜장', '탕수육', '짜장면', '돼지갈비찜', '제육볶음', '보쌈']
    TEST_ROOT = "../util/instagram_preprocessing/results/input_data.csv"
    results_name_list, result_score_list = foods_collaborative_filtering(foods_list,
                                                                         TEST_ROOT)
    print(results_name_list)
    print(result_score_list)