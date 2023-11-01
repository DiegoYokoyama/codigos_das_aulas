create database hub_innovation character set utf8mb4 collate utf8mb4_unicode_ci;
use hub_innovation;

create table palestras (
palestraID int auto_increment,
palestra_Tema varchar (100) not null,
palestra_vagas int,
palestra_descricao text (200),
primary key (palestraID)
);

create table palestrante (
palestranteID int,
palestrante_Nome varchar (50) not null,
linkedin_palestrante varchar(200),
imagem_palestrante varchar (200),
instagran_palestrante varchar (200),
constraint foreign key (palestranteID) references palestras(palestraID)
);

create table usuarios (
nome varchar (50) not null,
cpf varchar (14) not null,
email varchar (100) not null,
telefone varchar (15) not null,
data_De_Nascimento date not null,
genero varchar (20) not null,
consentimento bool not null,
palestra_ID int,
primary key (cpf),
constraint foreign key (palestra_ID) references palestras(palestraID)
);

create table salas (
sala varchar (30) not null,
salaID int auto_increment,
palestra_Sala int,
primary key (salaID),
constraint foreign key (palestra_Sala) references palestras(palestraID)
);

select * from palestras;
select * from usuarios;
select * from salas;

delimiter $

create trigger Tgr_Usuario_Insert after insert on usuarios
for each row
begin
update palestras set palestra_vagas = palestra_vagas - 1
where new.palestra_ID = palestraID;
end$

create trigger Tgr_Usuario_Delete after delete on usuarios
for each row
begin
update palestras set palestra_vagas = palestra_vagas + 1
where old.palestra_ID = palestraID;
end$

delimiter ; 

select * from palestras;

set sql_safe_updates = 0;