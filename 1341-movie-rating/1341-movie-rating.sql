# Write your MySQL query statement below
(SELECT name AS results
FROM Users u
JOIN MovieRating m ON u.user_id = m.user_id
GROUP BY m.user_id
ORDER BY COUNT(rating) DESC, name
LIMIT 1)

UNION ALL

(SELECT title AS results
FROM Movies m
JOIN MovieRating mr ON m.movie_id = mr.movie_id
WHERE YEAR(created_at) = 2020 AND MONTH(created_at) = 02
GROUP BY mr.movie_id
ORDER BY AVG(rating) DESC, title
LIMIT 1)