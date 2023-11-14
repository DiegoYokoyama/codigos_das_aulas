create database cadastrar character set utf8mb4 collate utf8mb4_unicode_ci; 
use cadastrar;

create table TelaDeCadastro(
id_nome int auto_increment,
nome varchar (50) not null,
email varchar (50) not null,
senha varchar (50) not null,
primary key (id_nome)
);



select * from TelaDeCadastro;