SELECT 
    q.query_name,
    ROUND(AVG(q.rating / q.position), 2) AS quality,
    ROUND(100.0 * SUM(CASE WHEN q.rating < 3 THEN 1 ELSE 0 END) / COUNT(*), 2) AS poor_query_percentage
FROM Queries q
GROUP BY q.query_name
ORDER BY quality DESC;
# yeah i used ai for help here.
