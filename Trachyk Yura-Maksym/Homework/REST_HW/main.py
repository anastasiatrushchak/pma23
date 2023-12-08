from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Початкові дані
initial_data = [
    {'id': 1, 'key': 'value1'},
    {'id': 2, 'key': 'value2'},
    {'id': 3, 'key': 'value3'}
]

data = {item['id']: item for item in initial_data}

@app.route('/api/resource', methods=['GET'])
def get_all_resources():
    return jsonify(list(data.values()))

@app.route('/api/resource/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    if resource_id in data:
        return jsonify(data[resource_id])
    else:
        return jsonify({'error': 'Resource not found'}), 404

stored_data = {}

@app.route('/api/data/store/<int:data_id>', methods=['POST'])
def post_data(data_id):
    try:
        data = request.get_json()
        stored_data[data_id] = data
        return jsonify({"message": f"Data with id {data_id} successfully stored.", "data": stored_data[data_id]})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/resource/update/<int:resource_id>', methods=['PATCH'])
def update_resource(resource_id):
    if resource_id in data:
        update_data = request.json
        data[resource_id].update(update_data)
        return jsonify(data[resource_id])
    else:
        return jsonify({'error': 'Resource not found'}), 404

@app.route('/api/resource/delete/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    if resource_id in data:
        deleted_data = data.pop(resource_id)
        return jsonify(deleted_data), 204
    else:
        return jsonify({'error': 'Resource not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
