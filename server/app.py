"""from flask import Flask, request, jsonify
import User
from database import db
from flask_cors import CORS



app = Flask(__name__)

CORS(app)
app.config['JSON_AS_ASCII'] = False



@app.route('/api', methods=['GET'])
def index():
    return {
        "channel": "The Show",
        "tutorial": "React, Flask and Docker"
    }


@app.route('/login', methods=['POST', 'GET'])
def login():
    name = request.json["inputUsername"]
    password = request.json["inputPassword"]
    user = userCollectionn.find_one({"name": name, "password": password})
    if user:
        #login successful
        db.users.insert_one({"email": name, "password": password})
        return jsonify({"message": "Login Successful"})
    else:
        #login failed
        return jsonify({"message": "Login Failed"})



userCollectionn = db["users"]
transactionCollection = db["trasactions"]

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') """

from flask import Flask, request, jsonify
import User
from database import db
from flask_cors import CORS



app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

userCollectionn = db["users"]
transactionCollection = db["trasactions"]

@app.route('/', methods=['GET'])
def get_data():
    data = {'key': 'value'}
    return jsonify(data)

@app.route('/register', methods=['POST'])
def index():

    
    inputUsername = request.json["inputUsername"]
    inputPassword = request.json["inputPassword"]
    user = userCollectionn.find_one({"name": inputUsername, "password": inputPassword})
    if user:
        #login successful
        db.users.insert_one({"email": inputUsername, "password": inputPassword})
        return jsonify({"message": "Registration Successful"})
    else:
        #login failed
        return jsonify({"message": "Registration Failed"})



@app.route('/login', methods=['POST'])
def login():
    inputUsername = request.json["inputUsername"]
    print(inputUsername)
    inputPassword = request.json["inputPassword"]
    user = userCollectionn.find_one({"name": inputUsername, "password": inputPassword})
    if user:
        #login successful
        db.users.insert_one({"email": inputUsername, "password": inputPassword})
    else:
        #login failed
        return jsonify({"message": "Login Failed"})



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)