# Write your MySQL query statement below
WITH cumulated AS(
    SELECT person_name, turn,
    SUM(weight) OVER (ORDER BY turn ASC) AS c_sum 
    FROM Queue
)

SELECT person_name
FROM cumulated
WHERE c_sum <= 1000
ORDER BY turn DESC
LIMIT 1
