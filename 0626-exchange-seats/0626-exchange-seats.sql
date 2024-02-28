# Write your MySQL query statement below
SELECT s1.id, 
CASE
    WHEN s1.id % 2 = 1
        THEN IFNULL((SELECT s2.student 
        FROM Seat s2
        WHERE s2.id = s1.id + 1), s1.student)
    ELSE (SELECT s3.student 
        FROM Seat s3 
        WHERE s3.id = s1.id - 1)
END AS student    
FROM Seat s1
-- JOIN Seat s2 ON s1.id = s2.id - 1
