create database titanic character set utf8mb4 collate utf8mb4_unicode_ci;
use titanic;

create table Passenger (
Passenger_ID int not null,
Survived varchar (1) not null,
Pclass int  not null,
Name varchar (150) not null,
Sex varchar (10) not null,
Age varchar (10),
SibSp varchar (1) not null,
Parch varchar (1) not null,
Ticket varchar (50) not null,
Fare varchar (20) not null,
Cabin varchar (50),
Embarked varchar (1) not null,
primary key (Passenger_ID)
);

select *from Passenger;

#quantas pessoas sobreviveu

select * from Passenger where survived = 1;
select sum(survived) from Passenger;
select count(*) from Passenger where age < 12 and survived = 1;
select count(*) from Passenger where Sex = 'female' and survived = 1;
select count(*) from Passenger where Sex = 'female' and survived = 0;
select count(*) from Passenger where Sex = 'male' and survived = 1;
select count(*) from Passenger where Sex = 'male' and survived = 0;

