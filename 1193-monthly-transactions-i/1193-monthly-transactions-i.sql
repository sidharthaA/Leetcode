# Write your MySQL query statement below
WITH cte AS
(SELECT country, state, amount, trans_date, 
CASE
    WHEN state = 'approved'
        THEN amount
    ELSE Null
END AS approved_amount
FROM Transactions)

SELECT DISTINCT DATE_FORMAT(trans_date, '%Y-%m') AS month, country, 
COUNT(*) AS trans_count, SUM(amount) AS trans_total_amount, 
COUNT(approved_amount) AS approved_count, IFNULL(SUM(approved_amount), 0) AS approved_total_amount
FROM cte
GROUP BY country, month