create database netflix character set utf8mb4 collate utf8mb4_unicode_ci; #caracteristica do banco de dados e um banco de dados que vc vai criar
use netflix; #e o banco de dados que vc deseja usar
create table usuario ( #vai criar uma tabela
nome varchar (50) not null,  #e um nome que vc vai criar dentro da tabela varchar e um caracter 
cpf varchar(14) not null, 
endereco varchar (50) not null, 
email varchar (40) unique, 
senha varchar (50) not null,
telefone varchar (15) not null,
cartao varchar (20) not null,
primary key (cpf)); # primery key e um numero unico que nao repeti

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

rename table video2 to video; #vai alterar o nome da tabela
alter table video change temporada2 temporada int  #vai alterar dentro da tabela que vc escolheu