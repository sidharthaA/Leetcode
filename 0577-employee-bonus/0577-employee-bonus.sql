# Write your MySQL query statement below
SELECT name, bonus FROM Employee
left JOIN Bonus ON Employee.empId = Bonus.empId
WHERE bonus < 1000 or bonus is Null