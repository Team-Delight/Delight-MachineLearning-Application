from flask import Flask, jsonify, request
from flask_cors import CORS

from model.collaborative_filtering import foods_collaborative_filtering, DATA_ROOT

app = Flask(__name__)
CORS(app)


@app.route('/api/ml-servers', methods=['POST'])
def find_ml_results():
    print(request.get_json())
    selected_foods = request.get_json()['foods']
    print(selected_foods)
    results_name_list, result_score_list = foods_collaborative_filtering(selected_foods, DATA_ROOT)

    return jsonify(
        {
            "foods": results_name_list,
            "scores": result_score_list
        }
    )


if __name__ == '__main__':
    app.run(port=9090)
