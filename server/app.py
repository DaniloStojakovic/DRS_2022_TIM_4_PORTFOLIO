from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    ime = db.Column("ime", db.String(100))
    mail = db.Column("mail", db.String(100), primary_key=True)
    adresa = db.Column("adresa", db.String(100))

    def __repr__(self):
        return "hello wolrd"

    def __init__(self, ime, mail, adresa):
        self.ime = ime
        self.mail = mail
        self.adresa = adresa

db.create_all()

@app.route('/api', methods=['GET'])
def index():
    return {
        "channel": "The Show",
        "tutorial": "React, Flask and Docker"
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')