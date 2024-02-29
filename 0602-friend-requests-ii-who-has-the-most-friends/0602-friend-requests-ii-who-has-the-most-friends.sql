-- # Write your MySQL query statement below
-- -- WITH cte1 AS (
-- --     SELECT requester_id, COUNT(accepter_id)
-- --     FROM RequestAccepted
-- --     GROUP BY requester_id
-- --     ORDER BY requester_id
-- -- )

-- -- WITH cte2 AS (
-- --     SELECT accepter_id, COUNT(requester_id)
-- --     FROM RequestAccepted
-- --     GROUP BY accepter_id
-- --     ORDER BY accepter_id
-- -- )
-- -- 

-- SELECT accepter_id , COUNT(requester_id) 
-- FROM RequestAccepted
-- GROUP BY accepter_id
-- -- ORDER BY accepter_id

-- UNION

-- SELECT requester_id AS id, COUNT(accepter_id) AS num
-- FROM RequestAccepted
-- GROUP BY requester_id
-- -- ORDER BY requester_id

SELECT id, COUNT(*) AS num 
FROM (
    SELECT requester_id AS id 
    FROM RequestAccepted 
    UNION ALL 
    SELECT accepter_id 
    FROM RequestAccepted 
) AS friend_request 
GROUP BY id
ORDER BY num DESC 
LIMIT 1;