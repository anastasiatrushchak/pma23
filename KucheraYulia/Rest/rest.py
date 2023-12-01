from flask import Flask, jsonify, request

app = Flask(__name__)

# Початкова структура даних (зразок)
data = {"id": 1, "name": "Sample"}

# GET метод для отримання даних
@app.route('/data', methods=['GET'])
def get_data():
    try:
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST метод для збереження даних
@app.route('/data', methods=['POST'])
def create_data():
    try:
        req_data = request.get_json()
        data.update(req_data)
        return jsonify(data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PATCH метод для оновлення даних
@app.route('/data', methods=['PATCH'])
def update_data():
    try:
        req_data = request.get_json()
        for key, value in req_data.items():
            if key not in data:
                data[key] = value
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE метод для видалення даних
@app.route('/data', methods=['DELETE'])
def delete_data():
    try:
        data.clear()
        return jsonify({"message": "Data deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)