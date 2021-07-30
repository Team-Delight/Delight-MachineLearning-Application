import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def make_input_data(data_path):
    food_info = pd.read_csv(data_path,encoding="utf-8")
    food_info['soup'] = food_info.apply(create_soup, axis=1)
    return food_info


def create_soup(food_info):
    ing = food_info['ingredients'].replace(",","").replace("[","").replace("]","").replace("'","")
    insta = food_info['instagram'].replace(",","").replace("[","").replace("]","").replace("'","")
    return ing+insta


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


def collaborative_filtering(title, data_path):

    food_info = make_input_data(data_path)
    count_matrix = make_count_vectorizer(food_info['soup'])

    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    indices = pd.Series(food_info.index, index=food_info['title'])

    results, sim_scores = get_recommendations(title, indices, cosine_sim, food_info)
    return results.tolist(), sim_scores

if __name__ == "__main__":
    recommendations, scores = collaborative_filtering("닭볶음탕", "./temp_data.csv")
    print(recommendations)
    print(scores)

    # 여러개 음식이 들어왔을때에 대한 로직 추가 필요