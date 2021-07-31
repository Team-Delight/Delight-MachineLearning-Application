from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def get_ml_results(selected_foods):
    pass


@app.route('/api/ml-servers', methods=['POST'])
def find_ml_results():
    selected_foods = request.form['foods']
    recommended_foods = get_ml_results(selected_foods)

    return jsonify(
        {
            "foods": recommended_foods
        }
    )


if __name__ == '__main__':
    app.run(port=9090)
