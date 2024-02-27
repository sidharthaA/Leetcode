# Write your MySQL query statement below
SELECT customer_id, count(Visits.visit_id) as count_no_trans from Visits
left JOIN Transactions ON Visits.visit_id = Transactions.visit_id
where Transactions.visit_id is Null
group by customer_id