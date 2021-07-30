import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def make_input_data(data_path):
    food_info = pd.read_csv(data_path)
    food_info['soup'] = food_info.apply(create_soup, axis=1)


def create_soup(food_info):
    '''
    type(food_info['ingredients']) =List<string>
    type(food_info['instagram_info']) =List<string>
    :return string
    '''
    return ' '.join(food_info['ingredients']) + ' ' + ' '.join(food_info['instagram_info'])


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
    return dataframe['title'].iloc[movie_indices]


def collaborative_filtering(title, data_path):

    food_info = pd.read_csv(data_path)
    make_input_data(food_info)
    count_matrix = make_count_vectorizer(food_info['soup'])

    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    indices = pd.Series(food_info.index, index=food_info['title'])

    results = get_recommendations(title, indices, cosine_sim, food_info)
    return list(results)
