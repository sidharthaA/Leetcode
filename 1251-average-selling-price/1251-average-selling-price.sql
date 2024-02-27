# Write your MySQL query statement below
SELECT p.product_id, IFNULL(ROUND(SUM(price * units) / sum(units), 2), 0) AS average_price 
FROM Prices p
LEFT JOIN UnitsSold u ON p.product_id = u.product_id AND 
                    p.end_date >= u.purchase_date AND 
                    p.start_date <= u.purchase_date
GROUP BY p.product_id