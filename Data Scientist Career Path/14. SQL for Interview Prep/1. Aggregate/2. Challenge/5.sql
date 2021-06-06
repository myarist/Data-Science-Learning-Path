SELECT user_id, 
   SUM(watch_duration_in_minutes) AS 'total_duration'
FROM watch_history
GROUP BY 1
HAVING total_duration > 400;