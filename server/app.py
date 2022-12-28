from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["animal_db"]
    return db

@app.route('/')
def ping_server():
    return "Welcome to K!@()_DK@!(D)K!@)(DK)."

@app.route('/animals')
def get_stored_animals():
    db = get_db()
    _animals = db.animal_tb.find()
    animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
    return jsonify({"animals": animals})


@app.route('/api', methods=['GET'])
def index():
    return {
        "channel": "The qwodpk",
        "tutorial": "qwdd, Flask and Docker"
    }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')