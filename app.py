from flask import Flask, jsonify, request
from flask_cors import CORS

from model.collaborative_filtering import foods_collaborative_filtering, DATA_ROOT

server = Flask(__name__)
CORS(server)


@server.route('/ml-servers', methods=['POST'])
def find_ml_results():
    selected_foods = request.get_json()['foods']
    results_name_list, result_score_list = foods_collaborative_filtering(selected_foods, DATA_ROOT)

    return jsonify(
        {
            "foods": results_name_list,
            "scores": result_score_list
        }
    )