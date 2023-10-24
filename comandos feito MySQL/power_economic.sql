create database power_economic character set utf8mb4 collate utf8mb4_unicode_ci;
use power_economic;

create table rank_Region(
ranked int auto_increment,
Country_Region varchar (150) not null,
primary key (ranked)
);

create table cost_of_living (
Cost_index float not null,
Monthly_income varchar (20) not null,
Purchasing_power_index float not null
);



select * from rank_Region;
select * from cost_of_living;


