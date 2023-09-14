create database casa character set utf8mb4 collate utf8mb4_unicode_ci;
use casa;

create table casa(
num_casa int auto_increment,
nome_da_rua varchar (50) not null,
numero_de_residente int not null,
proprietario varchar (50) not null,
primary key (num_casa)
);

describe casa;

insert into casa (nome_da_rua, numero_de_residente, proprietario) values ('rua 55', 5 , 'Diego');

