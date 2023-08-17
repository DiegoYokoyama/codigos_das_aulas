create database netflix character set utf8mb4 collate utf8mb4_unicode_ci;
use netflix;
create table usuario (
nome varchar (50) not null,
cpf varchar(14) not null, 
endereco varchar (50) not null, 
email varchar (40) unique, 
senha varchar (50) not null,
telefone varchar (15) not null,
cartao varchar (20) not null,
primary key (cpf));

create table mensalidade (
mes_ano date not null,
valor_pagar float not null,
data_pagar date not null,
primary key (mes_ano));

create table ator (
nome varchar (50) not null,
data_nascimento varchar (10) not null,
local_nascimento varchar (50),
primary key (nome));

create table video (
temporada int not null,
episodio int not null,
titulo varchar (50) not null,
ano int not null,
duracao float not null,
produtora varchar (50) not null,
tipo varchar (50) not null,
primary key (titulo));
