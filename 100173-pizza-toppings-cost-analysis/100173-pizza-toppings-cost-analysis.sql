# Write your MySQL query statement below
select concat(a.topping_name, ",", b.topping_name, ",", c.topping_name) as pizza,
a.cost+b.cost+c.cost as total_cost
from Toppings a
join Toppings b
on b.topping_name>a.topping_name
join Toppings c
on c.topping_name>b.topping_name
order by total_cost desc, pizza