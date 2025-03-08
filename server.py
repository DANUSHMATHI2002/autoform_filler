from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

@app.route('/data', methods=['GET'])
def get_data():
    if not os.path.exists(DATA_FILE):
        return jsonify({}), 200  # Return empty JSON if no data exists

    with open(DATA_FILE, "r") as file:
        try:
            data = json.load(file)
            return jsonify(data)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON file"}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
