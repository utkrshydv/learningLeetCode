# Write your MySQL query statement below
select NAME as Customers 
from Customers
where id NOT IN (select customerId from Orders);