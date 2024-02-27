# Write your MySQL query statement below
-- SELECT employee_id, department_id
-- FROM Employee
-- WHERE primary_flag = "Y"
-- UNION
-- SELECT employee_id, department_id
-- FROM Employee
-- GROUP BY employee_id
-- HAVING COUNT(department_id) = 1;

SELECT employee_id, department_id
FROM
    (SELECT *, COUNT(employee_id) OVER(PARTITION BY employee_id) AS employee_count
    FROM Employee) AS EmplyeePartition
WHERE primary_flag = "Y" OR employee_count = 1;