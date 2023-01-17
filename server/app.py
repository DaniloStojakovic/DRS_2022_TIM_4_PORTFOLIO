from flask import Flask, request, jsonify
import User
from database import db
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/api', methods=['GET'])

def index():
    return {
        "channel": "The Show",
        "tutorial": "React, Flask and Docker"
    }


userCollectionn = db["users"]
transactionCollection = db["trasactions"]

@app.route('/register', methods=['POST', 'GET'])
def register():
    # code to handle registration request

    email = request.json["email"]

    return jsonify({"message": "Registration Successful"})

@app.route('/login', methods=['GET', 'POST'])
def login():
    __name__ = request.json["name"]
    __password__ = request.json["input_passsword"]
    #user = userCollectionn.find_one({"name": __name__, "password": __password__})
    if 5 > 3:
        #login successful
        #db.users.insert_one({"email": __name__, "password": __password__})
        return jsonify({"message": "Login Successful"})
    else:
        #login failed
        return jsonify({"message": "Login Failed"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')