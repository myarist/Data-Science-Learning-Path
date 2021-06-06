SELECT first_name, COUNT(*) AS count
FROM users
GROUP BY first_name
ORDER BY count DESC;