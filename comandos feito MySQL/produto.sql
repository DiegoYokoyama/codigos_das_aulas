create database produto character set utf8mb4 collate utf8mb4_unicode_ci;
use produto;

create table produtos (
referencia varchar (3) primary key,
descricao varchar (50) unique,
estoque int not null default 0
);


insert into produtos values ('001','feijão',10);
insert into produtos values('002','arroz',5);
insert into produtos values('003','farinha',15);


create table itensvenda (
venda int,
produto varchar (3),
quantidade int
);

insert into itensvenda values(1,'001',3);
insert into itensvenda values(1,'002',1);
insert into itensvenda values(1,'003',5);

delimiter $
create trigger tgr_itensvenda_insert after insert
on itensvenda
for each row
begin
update produtos set estoque = estoque - new.quantidade where referencia = new.produto;
end$

show triggers$
select * from produtos$
insert into itensvenda values(1,'003',3);
delimiter $


select * from itensvenda$

create trigger tgr_itensvenda_delete after delete
on itensvenda
for each row 
begin 
update produtos set estoque = estoque + old.quantidade
where referencia = old.produto;
end$

delimiter ;

show triggers;

set sql_safe_updates = 0;

delete from itensvenda where produto = 002;


select * from itensvenda;
select * from produtos;
show triggers;

