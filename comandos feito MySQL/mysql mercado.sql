create database mercado character set utf8mb4 collate utf8mb4_unicode_ci;
use mercado;

create table fornecedor(
cod_fornecedor varchar (20) not null,
nome varchar (100) not null,
cidade_sede varchar (50) not null,
grupo_cod_fornecedor  varchar (10),
primary key (cod_fornecedor)
);
describe fornecedor;

create table material(
cod_material int auto_increment,
cod_fornecedor varchar (20) not null,
constraint foreign key (cod_fornecedor) references fornecedor(cod_fornecedor),
nome varchar (100) not null,
descricao varchar (100) not null,
primary key (cod_material)
);

describe material;
insert into fornecedor values 
('ABC','ABC Materiais Eletronicos','Vitoria',NULL),
('XYZ','XYZ Materiais de escritorio','Rio de Janeiro','Hix'),
('Hidra','Hidra Materiais Hidrawlicos','Sao Paolu','Hix'),
('Hix','Hidrax Materiais Elêtronicos e Hidrawlicos','Sao Pailo',NULL);

insert into material values
(123,'ABC','Tomada eletronica 10A Nova','Tomada eletronica 10A padrao novo'),
(124,'ABC','Disjuntor 25A','Disjuntor eletrico 25A'),
(345,'XYZ','Resma Papel A4','Resma papel branco A4'),
(346,'XYZ','Toner imp HR5522','Toner impressora HR4422'),
(678,'Hidra','Cano PVC 1/2','Cano PVC 1/2 pol'),
(679,'Hidra','Cano PVC 3/4','Cano PVC 3/4 pol'),
(680,'Hidra','Medidor hidr 1/2','Medidor Hidraulico 1/2 pol'),
(681,'Hidra','Joelho 1/2','Conector Joelho 1/2 pol'),
(682,'Hidra','Junta 1/2','Cano PVC 1/2 pol'),
(1234,'ABC','Tomada eletrica 20A Nova','Tomada eletrica 20A padrao novo'),
(2345,'XYZ','Caneta Azul','Caneta esferografica azul'),
(4567,'XYZ','Grampeador','Grampeador mesa pequena'),
(4568,'XYZ','Caneta Marca Texto Amarelo','Caneta Marca Texto amarelo'),
(4569,'XYZ','Lapis HB','Lapis Preto HB');

select * from material;
select * from fornecedor;
