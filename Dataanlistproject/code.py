# Create a file named app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/items', methods=['GET'])
def get_items():
    items = [
        {"id": 1, "name": "Warframe A"},
        {"id": 2, "name": "Warframe B"}
    ]
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
