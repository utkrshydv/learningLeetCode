# Write your MySQL query statement below

select today.id
from weather today
join weather yesterday
on today.recordDate = yesterday.recordDate + interval 1 day
where today.temperature > yesterday.temperature;