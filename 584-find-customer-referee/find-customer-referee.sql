# Write your MySQL query statement below
-- select name from Customer where referee_id <> 2 or referee_id is null;

select name from customer where coalesce(referee_id, -1) <> 2;