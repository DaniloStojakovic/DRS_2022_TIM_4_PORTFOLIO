create database cryptobug;
use cryptobug;
select * from purchase;
create table user(
id int auto_increment primary key,
Firstname varchar (50),
lastname varchar (50),
address varchar (200),
city varchar (50),
country varchar (40),
phonenumber varchar (20),
email varchar(500),
password varchar (500),
date varchar (300)
);
create table purchase(
id int auto_increment primary key,
coin varchar (50),
price int (50),
quantity int (60),
date varchar (300),
user_id int,
FOREIGN KEY (user_id) REFERENCES user(id)
);
create table profit(
id int auto_increment primary key,
totalprofit int (50),
user_id int,
coin_id int,
FOREIGN KEY (user_id) REFERENCES user(id),
FOREIGN KEY (coin_id) REFERENCES purchase(id)
);
truncate profit;
select * from profit;
select * from purchase;