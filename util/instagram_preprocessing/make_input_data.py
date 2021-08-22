import pandas as pd


def make_input_data(INSTAGRAM_ROOT, INGREDIENTS_ROOT):
    insta = pd.read_csv(INSTAGRAM_ROOT)
    ingredients = pd.read_csv(INGREDIENTS_ROOT, header=None)
    foods = pd.read_csv(FOODS_ROOT, header=None)

    ingredients_table = ingredients.iloc[:, 1:].rename(columns={1: "food_id"})
    food_table = foods[[0, 1]].rename(columns={0: "food_id", 1: "title"})

    food_ingredients = pd.merge(left=food_table, right=ingredients_table, how="inner", on="food_id")
    final_data = pd.merge(left=food_ingredients, right=insta)

    final_data["ingredients"] = make_series(final_data.iloc[:, 2:9])
    final_data["instagram"] = make_series(final_data.iloc[:, 9:-1])

    final_data[["title", "ingredients", "instagram"]].to_csv(SAVE_INPUT_DATA_ROOT, encoding="utf-8-sig",
                                                             index=False)


def make_series(df):
    outer_list = []
    for j in range(df.shape[0]):
        inner_list = []
        for i in df.iloc[j, :]:
            if type(i) is str:
                inner_list.append(i)
        outer_list.append(inner_list)
    return outer_list


if __name__ == "__main__":
    INSTAGRAM_ROOT = "./results/instagram_food_data.csv"
    INGREDIENTS_ROOT = "./dataset_from_java/delight_food_ingredients.csv"
    FOODS_ROOT = "./dataset_from_java/delight_food.csv"
    SAVE_INPUT_DATA_ROOT = "./results/input_data.csv"

    make_input_data(INSTAGRAM_ROOT, INGREDIENTS_ROOT)
