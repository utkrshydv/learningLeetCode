# Write your MySQL query statement below
select 
 d.name as Department,
 e.name as Employee,
 e.salary as Salary
 from
 Employee e
 join department d
 on e.departmentId = d.id
 where
 (e.salary, e.departmentID) in (
    select MAX(salary), departmentId from Employee
    GROUP BY departmentId 
 );