create database CadastroCliente character set utf8mb4 collate utf8mb4_unicode_ci;
use CadastroCliente;
drop database CadastroCliente;
create table Cliente(
CPF varchar (14) not null,
Nome varchar (50) not null,
RG varchar (12) not null,
Id_estado int not null,
Id_cidade int not null,
Id_sexo int not null,
Id_nacionalidade int not null,
Fone varchar (14)not null,
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

INSERT INTO Estado (Estado) VALUES
('Acre'),
('Alagoas'),
('Amapá'),
('Amazonas'),
('Bahia'),
('Ceará'),
('Distrito Federal'),
('Espírito Santo'),
('Goiás'),
('Maranhão'),
('Mato Grosso'),
('Mato Grosso do Sul'),
('Minas Gerais'),
('Pará'),
('Paraíba'),
('Paraná'),
('Pernambuco'),
('Piauí'),
('Rio de Janeiro'),
('Rio Grande do Norte'),
('Rio Grande do Sul'),
('Rondônia'),
('Roraima'),
('Santa Catarina'),
('São Paulo'),
('Sergipe'),
('Tocantins');

INSERT INTO Cidade (Cidade) VALUES

('Rio Branco'),
('Cruzeiro do Sul'),
('Sena Madureira'),
('Feijó'),
('Tarauacá'),

('Maceió'),
('Arapiraca'),
('Palmeira dos Índios'),
('Rio Largo'),
('Santana do Ipanema'),

('Macapá'),
('Santana'),
('Laranjal do Jari'),
('Oiapoque'),
('Porto Grande'),

('Manaus'),
('Parintis'),
('Itacoatiara'),
('Manacapuru'),
('Coari'),

('Salvador'),
('Feira de Santana'),
('Vitoria da Conquista'),
('Itabna'),
('Camaçari'),

('Fortaleza'),
('Crato'),
('Itapipoca'),
('Aracati'),
('Sobral'),

('Taguatinga'),
('Samambaia'),
('Guará'),
('Águas Claras'),
('Celiândia'),

('Vitória'),
('Linhares'),
('Guarapari'),
('Cachoeiro do Itapemirim'),
('Vilha Velha'),

('Goiânia'),
('Nerópolis'),
('Aparecida de Goiânia'),
('Anápolis'),
('Rio Verde'),

('São Luís'),
('Imperatriz'),
('Timon'),
('Caxias'),
('Codó'),

('Cuiabá'),
('Cuiabá'),
('Rondonópolis'),
('Sinop'),
('Tangará da Serra'),

('Campo Grande'),
('Dourados'),
('Três Lagoas'),
('Corumbá'),
('Ponta Porã'),

('Belo Horizonte'),
('Uberlândia'),
('Contagem'),
('Betim'),
('Juiz de Fora'),

('Belém'),
('Ananindeua'),
('Santarém'),
('Marabá'),
('Castanhal'),

('João Pessoa'),
('Campina Grande'),
('Santa Rita'),
('Patos'),
('Bayeux'),

('Curitiba'),
('Londrina'),
('Maringá'),
('Ponta Grossa'),
('Cascavel'),

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

('Palmas'),
('Araguaína'),
( 'Gurupi'),
('Porto Nacional'),
('Paraíso do Tocantins');

INSERT INTO Sexo(Sexo) VALUES
('Masculino'),
('Feminino'),
('Outros');

INSERT INTO Nacionalidade(Nacionalidade)  VALUES
('Brasileira'),
('Estrangeira');

INSERT INTO Raca(Raca)  VALUES
('Branca'),
('Parda'),
('Negra'),
('Amarela'),
('Indígena');

INSERT INTO Escolaridade(Escolaridade)  VALUES
('Sem Educação Formal'),
('Ensino Fundamental Incompleto'),
('Ensino Fundamental Completo'),
('Ensino Médio Incompleto'),
('Ensino Médio Completo'),
('Ensino Superior Incompleto'),
('Ensino Superior Completo'),
('Pós-Graduação');

select * from Cliente;

Insert into Cliente Values
('936.986.040-19','Lyesun','28.504.147-2',1,1,3,2,'(42)3765-2078',1,1),
('370.526.650-00','Logan','21.996.890-1',2,2,2,1,'(63)2847-3187',5,2),
('988.661.470-60','Nagan','24.205.778-0',3,3,2,1,'(81)2562-1167',2,3),
('823.958.250-85','Lobiohad','13.464.092-5',4,4,1,1,'(28)3634-5497',2,4),
('402.471.580-11','Linarliu','39.432.671-4',5,5,1,2,'(84)2607-1497',3,5),
('529.683.460-75','Delwuava','49.752.216-0',6,6,2,2,'(49)3336-8087',5,6),
('785.118.170-42','Belegon','34.105.282-6',7,7,3,1,'(98)2338-0349',4,7),
('827.008.430-10','Flovigurz','30.648.637-4',8,8,2,1,'(89)2013-0881',5,8),
('758.427.920-10','Kikyodub','21.671.756-5',9,9,1,1,'(79)2067-0187',3,6),
('942.357.520-06','Duboku','45.195.120-7',10,10,3,1,'(82)3585-3671',4,7),
('843.669.310-87','Wawoborn','10.333.170-0',11,11,1,2,'(28)3274-4739',3,4),
('570.869.690-79','Hahlougu','35.977.340-0',12,12,1,2,'(93)2167-4027',3,3),
('454.065.450-00','Haerak','33.253.382-7',13,13,2,2,'(71)3093-2922',2,2),
('336.166.880-86','Aranlu','23.064.005-9',14,14,3,1,'(89)3046-0682',2,1),
('417.873.520-99','Noguek','35.784.566-3',15,15,2,2,'(65)3309-3640',1,3),
('055.701.840-40','Vointizao','19.945.377-9',16,16,3,1,'(34)3535-5682',1,4),
('104.733.430-53','Fialu','21.783.080-8',17,17,1,2,'(93)2825-7294',1,6),
('635.810.620-11','Rubug','42.337.084-4',18,18,2,1,'(82)2352-1706',2,7),
('049.167.120-21','Brodbu','42.067.602-8',19,19,2,1,'(79)3214-3064',3,8),
('880.713.770-40','Zaorga','33.504.365-3',20,20,3,2,'(87)2676-1285',4,2);

select Cliente.Nome,Cidade.Cidade from Cliente INNER JOIN Cidade On Cliente.Id_cidade = Cidade.Id_cidade;
select Cliente.Nome,Estado.Estado from Cliente INNER JOIN Estado On Cliente.Id_estado = Estado.Id_estado;
select Cliente.Nome,Cliente.CPF,Raca.Raca from Cliente INNER JOIN Raca On Cliente.Id_raca = Raca.Id_raca;
select Cliente.Nome,Nacionalidade.Nacionalidade from Cliente INNER JOIN Nacionalidade On Cliente.Id_Nacionalidade = Nacionalidade.Id_Nacionalidade;
select Cliente.Nome,Escolaridade.Escolaridade from Cliente INNER JOIN Escolaridade On Cliente.Id_Escolaridade = Escolaridade.Id_Escolaridade;
select Cliente.Nome,Cidade.Cidade,Estado.Estado from Cliente INNER JOIN Cidade On Cliente.Id_Cidade = Cidade.Id_Cidade INNER JOIN Estado ON Cliente.Id_Estado = Estado.Id_Estado;
select Cliente.Nome,Cidade.Cidade,Estado.Estado,Cliente.Fone,Cliente.RG,Sexo.Sexo,Nacionalidade.Nacionalidade,Raca.Raca,Escolaridade.Escolaridade from Cliente INNER JOIN Cidade On Cliente.Id_Cidade = Cidade.Id_Cidade INNER JOIN Estado ON Cliente.Id_Estado = Estado.Id_Estado INNER JOIN Sexo on Cliente.Id_Sexo = Sexo.Id_Sexo INNER JOIN Nacionalidade On Cliente.Id_Nacionalidade = Nacionalidade.Id_Nacionalidade INNER JOIN Raca On Cliente.Id_raca = Raca.Id_raca INNER JOIN Escolaridade On Cliente.Id_Escolaridade = Escolaridade.Id_Escolaridade;


update Cidade Set Cidade = 'abaixo de m' where Cidade like 'a%' or Cidade like 'b%' or Cidade like 'c%' or Cidade like 'd%' or Cidade like 'e%'  or Cidade like 'f%'  or Cidade like 'g%' or Cidade like 'h%' or Cidade like 'i%' or Cidade like 'j%' or Cidade like 'k%' or Cidade like 'l%' or Cidade like 'm%' ;
update Cidade Set Cidade = 'acima de m' where Cidade like 'n%' or Cidade like 'o%' or Cidade like 'p%' or Cidade like 'q%' or Cidade like 'r%'  or Cidade like 's%'  or Cidade like 't%' or Cidade like 'u%' or Cidade like 'v%' or Cidade like 'w%' or Cidade like 'x%' or Cidade like 'y%' or Cidade like 'z%' ;

update Estado set Estado = 'Região Centro-Oeste' where Estado like 'Mato Grosso' or Estado like 'Goías' or Estado like 'Mato Grosso Do Sul' or Estado like 'Distrito Federal';
update Estado set Estado = 'Região Norte' where Estado like 'Para' or Estado like 'Amapá' or Estado like 'Roraima' or Estado like 'Amazonas' or Estado like 'Acre' or Estado like 'Rondônia' or Estado like 'Tocantins';
update Estado set Estado = 'Região Nordeste' where Estado like 'Maranhão' or Estado like 'Piauí' or Estado Like 'Bahia' or Estado like 'Sergipe' or Estado like 'Pernambuco' or Estado like 'Paraiba' or Estado like 'Rio Grande Do Norte' or Estado like 'Ceará' or Estado like 'Alagoas';
UPDATE Estado SET Estado = 'Região Sudeste' WHERE Estado like 'Minas Gerais' or Estado like 'São Paulo' or Estado like 'Rio de Janeiro' or Estado like 'Espirito Santo';
UPDATE Estado SET Estado = 'Região Sul' WHERE Estado like 'Paraná' or Estado like 'Santa Catarina' or Estado like 'Rio Grande do Sul';

UPDATE Nacionalidade SET nacionalidade = 'Fora do Brasil' WHERE Nacionalidade = 'Estrangeiro(a)';

UPDATE Raca SET Raca  = 'Seres Humanos' WHERE Raca  like 'Branco' OR Raca  like 'Negro' OR Raca  like 'Asiático' OR Raca  like 'Pardo' OR Raca  like 'Indigena';

UPDATE Escolaridade SET Escolaridade = 'Ensino Básico' WHERE Escolaridade like 'Analfabeto' OR  escolaridade like 'Fundamental Incompleto' OR Escolaridade like 'Fundamental Completo' OR escolaridade like 'Médio Completo' or escolaridade like 'Médio Incompleto';

UPDATE Escolaridade SET Escolaridade = 'Ensino Avançado' WHERE Escolaridade like 'Superior' OR Escolaridade like 'Pós-graduação' OR Escolaridade like 'Mestrado' OR Escolaridade like 'Doutorado';

select * from Cidade;
select * from Estado;
select * from Raca;
delete from Cidade where Cidade = 'Rio Branco';
set SQL_SAFE_UPDATES = 0;