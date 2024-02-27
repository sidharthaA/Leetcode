# Write your MySQL query statement below
SELECT A.name from Employee A
join Employee B on A.id = B.managerId
-- where count(B.id) >= 5
group by A.id
having count(A.id) >=5