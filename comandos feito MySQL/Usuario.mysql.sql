create database UserCadastro character set utf8mb4 collate utf8mb4_unicode_ci; 
use UserCadastro;

create table Usuario(
id_nome int auto_increment,
nome varchar (50) not null,
cpf varchar (14) not null,
endereco varchar (150) not null,
sexo varchar (20) not null,
idade int,
rg varchar (10),
email varchar (50) not null,
cidade varchar (50) not null,
estadoCivil varchar (100) not null,
escolaridade varchar (50) not null,
primary key (id_nome)
);



select * from Usuario;