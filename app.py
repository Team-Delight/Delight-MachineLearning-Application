from flask import Flask, jsonify, request
from flask_cors import CORS
from model.collaborative_filtering import foods_collaborative_filtering

app = Flask(__name__)
CORS(app)

@app.route('/api/Ml-servers', methods=['POST'])
def find_ml_results():
    java_server_json_data = request.get_json()
    selected_foods = java_server_json_data["foods"]
    data_root = "./model/temp_data.csv"
    recommended_foods = foods_collaborative_filtering(selected_foods, data_root)

    return jsonify(
        {
            "foods": recommended_foods
        }
    )


if __name__ == '__main__':
    app.run(host="localhost",port=9090, debug=True)