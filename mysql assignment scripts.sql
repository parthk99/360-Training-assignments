#Exercise 1
create database HotelManagementSystem;

create table Customers (
cust_ID int, 
Cust_Name varchar(250), 
Cust_City varchar(250), 
Cust_RoomNo int,
CheckIn_Time datetime) ; 

insert into customers 
values ( 1, "John", "Miami", 5, "2022-09-19 00:00:00"),
(2, "Justin", "NYC", 4, "2022-09-18 00:00:01"),
(3, "James", "Boston", 3, "2022-09-19 00:00:02"), 
(4, "jason", "Vermont", 2, "2022-09-19 00:00:03"), 
(5, "Henry", "Hamptons", 1, "2022-09-19 00:00:04") ; 
select * from customers

#Exercise 2
select distinct(city) from customers;
select count(city) from customers;

Select MIN(quantity)
From order_details
Select max(quantity)
from order_details

select avg(quantity)
from order_details 
select sum(quantity)
from order_details 

select distinct(productname) from products limit 5, 15;

select * from suppliers 
where suppliername like "_a%"

select * from customers
where country not between "usa" and "canada";

select * from order_details 
where 

select * from orders
where orderdate like "2020-01-01" and "2021-01-01";
select * from orders
order by OrderDate desc;

select * from employees
where LastName not in ("sanjay", "Soniya");

create table supplierdetail as select * from suppliers;
select * from supplierdetail

delete from customers where country = "venezuela"; 
select * from customers







 



