from flask import Flask, request, jsonify
import User
from database import db
from flask_cors import CORS



app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

app.config["SECRET_KEY"] = "004f2af45d3a4e161a7dd2d17fdae47f"

userCollectionn = db["users"]
transactionCollection = db["trasactions"]

@app.route('/', methods=['GET'])
def get_data():
    data = {'key': 'value'}
    return jsonify(data)

@app.route('/register', methods=['POST'])
def index():
    userCollectionn.insert_one({"email", "password"})

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