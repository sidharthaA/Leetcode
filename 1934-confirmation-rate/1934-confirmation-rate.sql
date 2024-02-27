# Write your MySQL query statement below
select signups.user_id, IFNULL(ROUND(SUM(action = 'confirmed')/count(*), 2), 0) AS confirmation_rate 
from confirmations
right join Signups on signups.user_id = confirmations.user_id
group by signups.user_id