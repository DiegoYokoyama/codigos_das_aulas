create database cliente_voo character set utf8mb4 collate utf8mb4_unicode_ci;
use cliente_voo;

create table cliente(
nome varchar (50) not null,
destino varchar (50) not null,
fone varchar (15) not null
);

insert into cliente (nome,destino,fone) values 
('diego', 'sao paulo', '123456789'),
('evandro', 'campo grande', '987654'),
('felipe', 'sao paulo', '85854854');

select * from cliente where destino = 'sao paulo';


