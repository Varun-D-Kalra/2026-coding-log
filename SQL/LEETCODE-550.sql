# CTE FUNC TO SELECT UID AND THEIR LOGIN DATE
  
WITH log_date AS(
    SELECT DISTINCT(player_id), MIN(event_date) AS first_eve_date
    FROM Activity
    GROUP BY player_id
)

SELECT(ROUND(
     (SUM(CASE WHEN a.event_date = DATE_ADD(l.first_eve_date, INTERVAL 1 DAY) THEN 1 ELSE 0 END)
    / COUNT(DISTINCT(l.player_id))), 2)
    
) AS fraction
FROM Activity a
INNER JOIN log_date l
ON l.player_id = a.player_id
