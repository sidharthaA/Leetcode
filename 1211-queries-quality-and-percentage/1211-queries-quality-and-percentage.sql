# Write your MySQL query statement below
WITH cte AS
(SELECT query_name, rating / position AS ratio, 
CASE 
    WHEN rating < 3 
        then 1
    ELSE 0
END AS poor_query
FROM Queries)

SELECT query_name, ROUND(AVG(ratio), 2) AS quality, ROUND((SUM(poor_query) / COUNT(*)) * 100, 2) AS poor_query_percentage
FROM cte
GROUP BY query_name
HAVING query_name IS NOT Null