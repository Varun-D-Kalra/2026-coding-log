SELECT class
FROM Courses 
GROUP BY class
HAVING COUNT(class) >= 5;

# under 1 min ahaahaa
