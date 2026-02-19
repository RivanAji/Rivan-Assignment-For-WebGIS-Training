from flask import Flask, jsonify
import json
import os
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IKL_PATH = os.path.join(BASE_DIR, "output_geojson", "indeks_kualitas_lingkungan.geojson")

@app.route('/api/ikl', methods=['GET'])
def get_ikl():
    with open(IKL_PATH, "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# ===== cara run =====
# cd "Assignment/Rivan-Assignment 6" 
# ../../.venv/bin/python "Rivan - API_ikl.py"