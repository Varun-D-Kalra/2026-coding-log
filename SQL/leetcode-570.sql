SELECT name
FROM Employee e1
WHERE id in (
    SELECT managerId
    FROM Employee e2
    GROUP BY managerId
    HAVING COUNT(managerId) >= 5
)
