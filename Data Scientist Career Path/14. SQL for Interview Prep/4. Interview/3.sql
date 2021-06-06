SELECT genre, SUM(reviews) 
FROM apps
GROUP BY genre
HAVING SUM(reviews) > 30000000;