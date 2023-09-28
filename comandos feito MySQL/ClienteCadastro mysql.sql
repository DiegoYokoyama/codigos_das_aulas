create database ClienteCadastro character set utf8mb4 collate utf8mb4_unicode_ci;
use ClienteCadastro;
drop database ClienteCadastro;
create table Cliente(
CPF varchar (14) not null,
Nome varchar (50) not null,
RG varchar (12) not null,
Id_estado int not null,
Id_cidade int not null,
Id_sexo int not null,
Id_nacionalidade int not null,
Fone varchar (10)not null,
Id_raca int not null,
Id_escolaridade int not null,
constraint foreign key (Id_escolaridade) references Escolaridade(Id_escolaridade),
constraint foreign key (Id_estado) references Estado(Id_estado),
constraint foreign key (Id_raca) references Raca(Id_raca),
constraint foreign key (Id_nacionalidade) references Nacionalidade(Id_nacionalidade),
constraint foreign key (Id_Sexo) references Sexo(Id_Sexo),
constraint foreign key (Id_cidade) references Cidade(Id_cidade),
primary key (CPF)

);

create table Estado(
Id_estado int AUTO_INCREMENT,
Estado varchar (50) not null,
primary key (Id_estado)
);

create table Cidade(
Id_cidade int AUTO_INCREMENT,
Cidade varchar (50) not null,
primary key (Id_cidade)
);

create table Sexo(
Id_sexo int AUTO_INCREMENT,
Sexo varchar (20) not null,
primary key (Id_sexo)
);

create table Nacionalidade(
Id_nacionalidade int AUTO_INCREMENT,
Nacionalidade varchar (50) not null,
primary key (Id_nacionalidade)
);

create table Raca(
Id_raca int AUTO_INCREMENT,
Raca varchar (50) not null,
primary key (Id_raca)
);

create table Escolaridade(
Id_escolaridade int AUTO_INCREMENT,
Escolaridade varchar (50) not null,
primary key (Id_escolaridade)
);

INSERT INTO Estado VALUES

(1, 'Rio Branco'),
(2, 'Cruzeiro do Sul'),
(3, 'Sena Madureira'),
(4, 'Feijó'),
(5, 'Tarauacá'),

(6, 'Maceió'),
(7, 'Arapiraca'),
(8, 'Palmeira dos Índios'),
(9, 'Rio Largo'),
(10, 'Santana do Ipanema'),

(11, 'Macapá'),
(12, 'Santana'),
(13, 'Laranjal do Jari'),
(14, 'Oiapoque'),
(15, 'Porto Grande'),

(16, 'Manaus'),
(17, 'Parintis'),
(18, 'Itacoatiara'),
(19, 'Manacapuru'),
(20, 'Coari'),

(21, 'Salvador'),
(22, 'Feira de Santana'),
(23, 'Vitoria da Conquista'),
(24, 'Itabna'),
(25, 'Camaçari'),

(26, 'Fortaleza'),
(27, 'Crato'),
(28, 'Itapipoca'),
(29, 'Aracati'),
(30, 'Sobral'),

(31, 'Taguatinga'),
(32, 'Samambaia'),
(33, 'Guará'),
(34, 'Águas Claras'),
(35, 'Celiândia'),

(36, 'Vitória'),
(37, 'Linhares'),
(38, 'Guarapari'),
(39, 'Cachoeiro do Itapemirim'),
(40, 'Vilha Velha'),

(41, 'Goiânia'),
(42, 'Nerópolis'),
(43, 'Aparecida de Goiânia'),
(44, 'Anápolis'),
(45, 'Rio Verde'),

(46, 'São Luís'),
(47, 'Imperatriz'),
(48, 'Timon'),
(49, 'Caxias'),
(50, 'Codó'),

(51, 'Cuiabá'),
(52, 'Cuiabá'),
(53, 'Rondonópolis'),
(54, 'Sinop'),
(55, 'Tangará da Serra'),

(56, 'Campo Grande'),
(57, 'Dourados'),
(58, 'Três Lagoas'),
(59, 'Corumbá'),
(60, 'Ponta Porã'),

(61, 'Belo Horizonte'),
(62, 'Uberlândia'),
(63, 'Contagem'),
(64, 'Betim'),
(65, 'Juiz de Fora'),

(66, 'Belém'),
(67, 'Ananindeua'),
(68, 'Santarém'),
(69, 'Marabá'),
(70, 'Castanhal'),

(71, 'João Pessoa'),
(72, 'Campina Grande'),
(73, 'Santa Rita'),
(74, 'Patos'),
(75, 'Bayeux'),

(76, 'Curitiba'),
(77, 'Londrina'),
(78, 'Maringá'),
(79, 'Ponta Grossa'),
(80, 'Cascavel'),

('Recife'),
('Jaboatão dos Guararapes'),
('Olinda'),
('Caruaru'),
('Petrolina'),

('Teresina'),
('Parnaíba'),
('Picos'),
('Floriano'),
('Piripiri'),

('Rio de Janeiro'),
('São Gonçalo'),
('Duque de Caxias'),
('Nova Iguaçu'),
('Niterói'),

('Natal'),
('Mossoró'),
('Parnamirim'),
('São Gonçalo do Amarante'),
('Macaíba'),

('Porto Alegre'),
('Caxias do Sul'),
('Canoas'),
('Pelotas'),
('Santa Maria'),

('Porto Velho'),
('Ji-Paraná'),
('Ariquemes'),
('Vilhena'),
('Cacoal'),

('Boa Vista'),
('Rorainópolis'),
('Bonfim'),
('Mucajaí'),
('Caracaraí'),

('Florianópolis'),
('Joinville'),
('Blumenau'),
('São José'),
('Criciúma'),

('São Paulo'),
('Guarulhos'),
('Campinas'),
('São Bernardo do Campo'),
('Santo André'),

('Aracaju'),
('Nossa Senhora do Socorro'),
('Lagarto'),
('Itabaiana'),
('São Cristóvão'),

('Palmas')
('Araguaína')
( 'Gurupi')
('Porto Nacional')
('Paraíso do Tocantins'
);



INSERT INTO Nacionalidade  VALUES
('Brasileira'),
('Estrangeira');

INSERT INTO Raca  VALUES
('Branca'),
('Parda'),
('Negra'),
('Amarela'),
('Indígena');

INSERT INTO Escolaridade  VALUES
('Sem Educação Formal'),
('Ensino Fundamental Incompleto'),
('Ensino Fundamental Completo'),
('Ensino Médio Incompleto'),
('Ensino Médio Completo'),
('Ensino Superior Incompleto'),
('Ensino Superior Completo'),
('Pós-Graduação');

Insert into Cliente Values
('936.986.040-19','Lyesun','28.504.147-2',
('370.526.650-00','Logan','21.996.890-1',
('988.661.470-60','Nagan','24.205.778-0',
('823.958.250-85','Lobiohad','13.464.092-5',
('402.471.580-11','Linarliu','39.432.671-4',
('529.683.460-75','Delwuava','49.752.216-0',
('785.118.170-42','Belegon','34.105.282-6',
('827.008.430-10','Flovigurz','30.648.637-4',
('758.427.920-10','Kikyodub','21.671.756-5',
('942.357.520-06','Duboku','45.195.120-7',
('843.669.310-87','Wawoborn','10.333.170-0',
('570.869.690-79','Hahlougu','35.977.340-0',
('454.065.450-00','Haerak','33.253.382-7',
('336.166.880-86','Aranlu','23.064.005-9',
('417.873.520-99','Noguek','35.784.566-3',
('055.701.840-40','Vointizao','19.945.377-9',
('104.733.430-53','Fialu','21.783.080-8',
('635.810.620-11','Rubug','42.337.084-4',
('049.167.120-21','Brodbu','42.067.602-8',
('880.713.770-40','Zaorga','33.504.365-3',