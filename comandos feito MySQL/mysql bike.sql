create database bike character set utf8mb4 collate utf8mb4_unicode_ci; #caracteristica do banco de dados e um banco de dados que vc vai criar;
use bike;
create table Acct_Typ_Cd_LU_Tab (
Acct_Code int auto_increment,
Account_Type varchar (50) not null,
primary key (Acct_Code));

create table Customer (
Customer_ID int auto_increment,
Customer_Lname varchar (50) not null,
Customer_Fnome varchar (20) not null,
Cust_street varchar (50) not null,
Cust_city varchar (50) not null,
Cust_zip int (5)not null,
Cust_phone varchar (15) not null,
Fox_phone varchar (15),
primary key (Customer_ID));
describe Customer; # ve a tabela

create table State_lkup (
St_code int auto_increment,
State_nome varchar (50) not null,
primary key (St_code));

create table Supplier (
Supplier_ID int auto_increment,
Supplier_name varchar (50) not null,
Sup_street varchar (50) not null,
Sup_city varchar (50) not null,
Sup_zip int (5) not null,
Sup_phone varchar (15) not null,
Sup_fax varchar (15),
primary key (Supplier_ID));
describe Supplier;

create table Customer_Account (
Customer_ID int auto_increment,
Last_purch_dte date not null,
Last_pymt_dte date not null,
Last_acct_trans_dte date not null,
Acct_balance float not null,
primary key (Customer_ID));

create table Transaction_code (
Trans_code int not null,
Transaction_code varchar (50) not null,
primary key (Trans_code));

create table Customer_Acct_Hust1 (
Customer_ID int auto_increment,
Trans_dte date not null,
Old_acct_balance float not null,
New_acct_balance float not null,
primary key (Customer_ID));

create table Puchase_Order (
Seq_ID int auto_increment,
Purch_dte date not null,
serial_num int (12) not null,
Quantily float not null,
price float not null,
primary key (Seq_ID));

create table Parts_Inventory (
Bar_Code int not null,
Part_name varchar (50) not null,
Prt_description varchar (50) not null,
Prt_cost float not null,
Prt_prece float not null,
Quantity float not null,
primary key (Bar_Code));

create table Bike_Description (
Model_ID int not null,
Model_name varchar (20) not null,
Inv_price float not null,
Sale_Price float not null,
Description varchar (50) not null,
primary key (Model_ID));

create table Bike_Inventory (
Seq_ID int not null,
Serial_Number int not null,
Inventory_dte date not null,
primary key (Seq_ID));