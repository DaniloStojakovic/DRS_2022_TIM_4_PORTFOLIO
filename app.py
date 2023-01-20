from api import Crypto
from sqlalchemy import func
from flask import Flask, render_template,request, make_response,redirect,url_for
import math,smtplib,os
from datetime import timedelta,datetime
from flask_login import LoginManager, login_required,UserMixin, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
crypto  = Crypto()
bcrypt = Bcrypt()
bcrypt.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:durent2802@localhost/cryptobug"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key="aljiorweru0288402374"


db = SQLAlchemy(app)

class User(db.Model,UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    phonenumber = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    
    def __init__(self, firstname, lastname, address,city,country,phonenumber,email, password,date):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.city = city
        self.country = country
        self.phonenumber = phonenumber
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.date = dt_string
        
class Purchase(db.Model):
    __tablename__ = "purchase"
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    coin = db.Column(db.String,nullable=False)
    price = db.Column(db.Integer,nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    date = db.Column(db.String,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
class Profit(db.Model):
    __tablename__ = "profit"
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    totalprofit = db.Column(db.Integer,nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    coin_id = db.Column(db.Integer, db.ForeignKey("purchase.id"))

login = LoginManager()
login.init_app(app)
login.login_view = '/login'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/login',methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    error = None
    if (request.method=='POST'):
        email = request.form.get('mail')
        password = request.form.get('pwd')
        check = User.query.filter_by(email = email).first()
        if check is not None and bcrypt.check_password_hash(check.password,password):
            check.UserIn = True
            db.session.add(check)
            db.session.commit()
            login_user(check)
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid Email Or Password 🤨"
    return render_template('login.html',error=error),404

@app.route('/profile',methods=['POST','GET'])
@login_required
def profile():
    if request.method=='POST':
        address=request.form.get('address')
        city=request.form.get('city')
        country=request.form.get('country')
        phone=request.form.get('phonenumber')
        update = User.query.filter_by(email=current_user.email).first()
        update.address = address
        update.city = city
        update.country = country
        update.phonenumber = phone
        db.session.commit()
    return render_template('profile.html'),404

@app.route('/register',methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    error2 = None
    sucess = None
    error3 = None
    if request.method=='POST':
        name=request.form.get('name')
        surname=request.form.get('surname')
        address=request.form.get('address')
        city=request.form.get('city')
        country=request.form.get('country')
        phone=request.form.get('phone')
        email=request.form.get('mail')
        password = request.form.get('pwd')
        checkpassword = request.form.get('checkpwd')
        getid = User.query.filter_by(email=email).first()
        if getid:
            error2 = "Email Already Exists"
        elif password != checkpassword:
            error3 = "Password Doesn't Match"
        else:
            add = User(firstname=name,lastname=surname,address=address,city=city,country=country,phonenumber=phone,email=email,password=password,date=dt_string)
            db.session.add(add)
            db.session.commit()
            sucess = "Congratulations, login sucess!"
    return render_template('register.html',error2=error2,error3=error3,sucess=sucess),404



@app.route('/dashboard/')
@login_required
def dashboard():
    results = crypto.get_top_5()
    last = math.ceil(len(results)/int(100))
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page= int(page)
    results = results[(page-1)*int(100): (page-1)*int(100)+ int(100)]
    if (page==1):
        prev = "#"
        next = "/?page="+ str(page+1)
    elif(page==last):
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)
    return render_template('dashboard.html',page=page,prev=prev,next=next, results=results),404

@app.route('/purchase',methods=['POST','GET'])
def purchase():
    if request.method=='POST':
        coin=request.form.get('coin')
        price=request.form.get('price')
        quantity=request.form.get('quantity')
        date=request.form.get('date')
        data = Purchase(coin=coin,price=price,quantity=quantity,date=date,user_id=current_user.id)
        db.session.add(data)
        db.session.commit()
        data3 = Purchase.query.filter_by(coin=coin,user_id=current_user.id).first()
        price1 = data3.price
        quantity1 = data3.quantity
        total = price1*quantity1
        data1 = Profit(totalprofit=total,user_id=current_user.id,coin_id=data3.id)
        print(data3)
        db.session.add(data1)
        db.session.commit()
    return redirect(url_for('wallet'))
@app.route("/")
def main():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))    
    results = crypto.get_top_5()
    last = math.ceil(len(results)/int(100))
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page= int(page)
    results = results[(page-1)*int(100): (page-1)*int(100)+ int(100)]
    if (page==1):
        prev = "#"
        next = "/?page="+ str(page+1)
    elif(page==last):
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)
    return render_template('index.html',page=page,prev=prev,next=next, results=results)

@app.route("/coin/<id>/<name>/<symbol>/<cmc_rank>/<num_market_pairs>/<circulating_supply>/<total_supply>/<max_supply>/<last_updated>/<date_added>/<price>/<volume_24h>/<volume_change_24h>/<percent_change_1h>/<percent_change_24h>/<percent_change_7d>/<market_cap>/<market_cap_dominance>/<fully_diluted_market_cap>")
def coin(id,name,symbol,cmc_rank,num_market_pairs,circulating_supply,total_supply,max_supply,last_updated,date_added,price,volume_24h,volume_change_24h,percent_change_1h,percent_change_24h,percent_change_7d,market_cap,market_cap_dominance,fully_diluted_market_cap):
    return render_template('details.html', id=id,name=name,symbol=symbol,cmc_rank=cmc_rank,num_market_pairs=num_market_pairs,circulating_supply=float(circulating_supply),total_supply=float(total_supply),max_supply=max_supply,last_updated=last_updated,date_added=date_added,price=float(price),volume_24h=volume_24h,volume_change_24h=float(volume_change_24h),percent_change_1h=float(percent_change_1h),percent_change_24h=float(percent_change_24h),percent_change_7d=float(percent_change_7d),market_cap=float(market_cap),market_cap_dominance=float(market_cap_dominance),fully_diluted_market_cap=float(fully_diluted_market_cap))

@app.route("/coin/<id>/<name>/<symbol>/<cmc_rank>/<num_market_pairs>/<circulating_supply>/<total_supply>/<max_supply>/<last_updated>/<date_added>/<price>/<volume_24h>/<volume_change_24h>/<percent_change_1h>/<percent_change_24h>/<percent_change_7d>/<market_cap>/<market_cap_dominance>/<fully_diluted_market_cap>/user")
@login_required
def coin_2(id,name,symbol,cmc_rank,num_market_pairs,circulating_supply,total_supply,max_supply,last_updated,date_added,price,volume_24h,volume_change_24h,percent_change_1h,percent_change_24h,percent_change_7d,market_cap,market_cap_dominance,fully_diluted_market_cap):
    return render_template('details_2.html', id=id,name=name,symbol=symbol,cmc_rank=cmc_rank,num_market_pairs=num_market_pairs,circulating_supply=float(circulating_supply),total_supply=float(total_supply),max_supply=max_supply,last_updated=last_updated,date_added=date_added,price=float(price),volume_24h=volume_24h,volume_change_24h=float(volume_change_24h),percent_change_1h=float(percent_change_1h),percent_change_24h=float(percent_change_24h),percent_change_7d=float(percent_change_7d),market_cap=float(market_cap),market_cap_dominance=float(market_cap_dominance),fully_diluted_market_cap=float(fully_diluted_market_cap))


@app.route('/wallet/')
@login_required
def wallet():
    search = Purchase.query.filter_by(user_id=current_user.id).all()
    count = db.session.query(Purchase).filter_by(user_id=current_user.id).count()
    total_sum = db.session.query(func.sum(Purchase.quantity)).filter_by(user_id=current_user.id).scalar()
    price = db.session.query(func.sum(Profit.totalprofit)).filter_by(user_id=current_user.id).scalar()
    return render_template('wallet.html',search=search,count=count,total_sum=total_sum,price=price),404

@app.route("/logout",methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))   

@app.route("/deleteCoin",methods=['POST'])
@login_required
def deleteCoin():
    if request.method=='POST':
        id = request.form.get('Id')
        Purchase.query.filter_by(id=id,user_id=current_user.id).delete()
        print(id)
        db.session.commit()
        Profit.query.filter_by(coin_id=id,user_id=current_user.id).delete()
        print(id)
        db.session.commit()
    return redirect(url_for('wallet'))

@app.route("/SellCoin",methods=['POST'])
@login_required
def SellCoin():
    if request.method=='POST':
        id = request.form.get('Id')
        Purchase.query.filter_by(id=id,user_id=current_user.id).delete()
        db.session.commit()
    return redirect(url_for('wallet'))


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)


