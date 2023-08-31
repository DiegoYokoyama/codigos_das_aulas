create database ecommerce; #faltou o (a) no database
use ecommerce;
#faltou aspas no produtos e tirar a virgula do id fabrica
create table  produtos(
    id_prod int auto_increment not null,
    nome_prod varchar(100) not null,
    descricao text,
    modelo varchar(50),
    id_categoria int(5),
    id_fabricante int(5),
    primary key (id_prod) #adicionei um primary key
    );
    describe produtos;
	drop table estoque_produtos;
    
create table clientes (
    id_cli int auto_increment not null, #auto incremente tem que ser int nao varchar
    nome varchar(100) not null,
    cpf int(11),
    telefone varchar(50),
    sexo enum('F','M'),
    cadastro datetime,
    constraint primary key (id_cli)); 
    

create table pedidos(
	num_pedido int auto_increment not null,
	data datetime,
	status varchar(50),
	id_cli int,
	constraint primary key (num_pedido),
	constraint foreign key (id_cli) references clientes(id_cli)
    );

    #faltou l no table
	create table pedido_item(
	idtem_pedido int auto_increment not null,
	num_pedido int not null,
    qtde int(5) not null,
    valor_unit decimal(10,2),
    total decimal(10,2),
    id_prod int not null,
    constraint primary key (idtem_pedido),
    constraint foreign key (num_pedido) references pedidos(num_pedido), #tirei o n e adicionei um n no final
    constraint foreign key (id_prod) references produtos(id_prod)
    );

    create table estoque_produtos(
		id_estoque int auto_increment not null,
        quantidade int(5) not null,
        quant_min int(5),
        id_prod int(5), #faltou um aspas depois do 5
        constraint primary key (id_estoque),
		constraint foreign key (id_prod) references produtos(id_prod)
        );
	insert into clientes values (null,'João','02102202324','6799999999','M',now()); #coloquei o insert info para baixo e coloquei um s no clientes
    insert into clientes values (null,'Tadeu','02102202366','6799999999','M',now()); #arrumei o insert
    insert into clientes values (null,'Francisco','02102202399','6799999999','M',now());
    insert into clientes values (null,'Maria','02102202377','6799999999','F',now());
    insert into clientes values (null,'Antonia','02102202388','6799999999','F',now());
    
	insert into produtos values (null,'Notebook Dell','Core i5,8GB,SDD 240GB','Inspirion 1500',null,null);
    insert into produtos values (null,'Notebook Acer','Core i5,8GB,SDD 240GB','Aspire T',null,null);
    insert into produtos values (null,'Notebook Asus','Core i5,8GB,SDD 240GB','A95Z',null,null);
    insert into produtos values (null,'Notebook Apple','Core i7, 16GB, SDD 512GB','BookPRo',null,null);
    insert into produtos values (null,'Notebook Positivo','Celerom,4GB,HD 1TB','POS8080',null,null);
    
    insert into produtos values (null,'Placa-Mãe ASUS','Onboard','P',null,null);
    insert into produtos values (null,'Processador AMD','4.2Ghz','Ryzen5',null,null); #faltou uma virgula depois do processador


    insert into produtos values (null,'Placa de Vídeo RADEON','8GB','RX5500',null,null);
    insert into produtos values (null,'Fonte Corsair','Selo 80plus','CX1200W',null,null);

    
	select * from produtos;
    describe estoque_produtos; #tirei o l do describle


	insert into estoque_produtos values (1,80,10,1); 
    insert into estoque_produtos values (2,44,5,9); #tirei o null e adicionei o s no final do produtos
    insert into estoque_produtos values (3,55,5,8);
    insert into estoque_produtos values (4,36,5,7);
    insert into estoque_produtos values (5,49,5,6);
    insert into estoque_produtos values (6,100,5,1);
    insert into estoque_produtos values (7,100,5,2);
    insert into estoque_produtos values (8,100,5,3);
    insert into estoque_produtos values (9,100,5,4);
    insert into estoque_produtos values (10,100,5,5);
	
    insert into clientes values(null,'diego','02102202324','6799999999','M',now())