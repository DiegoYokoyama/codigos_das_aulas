create database universidade;
use universidade;

create table departamento(
nome varchar (50) not null,
codigo int auto_increment not null,
telefone varchar (20),
centro varchar (50) not null,
primary key (codigo)
);

drop table departamento;

create table aluno(
nome varchar (50) not null,
numero_de_matricula int auto_increment not null,
cpf varchar(15) not null,
endereco text,
telefone varchar (20) not null,
second_telefone varchar (20),
data_de_nascimento date not null,
sexo enum('F','M') not null,
departamento varchar (50) not null,
curso varchar (50) not null,
primary key (numero_de_matricula)
);

create table curso (
nome varchar (50) not null,
tipo varchar (50) not null,
departamento varchar (50) not null,
coordenador varchar (50) not null,
vice_coordenador varchar (50) not null
);

create table professor (
nomr varchar (50) not null,
cpf varchar (15) not null,
departamento varchar (50) not null,
telefone varchar (20) not null,
primary key (cpf)
);