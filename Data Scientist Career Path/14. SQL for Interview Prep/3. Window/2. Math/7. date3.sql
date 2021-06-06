SELECT STRFTIME(format, timestring, modifier1, modifier2, ...)
SELECT STRFTIME('%m %Y', 'now');
SELECT STRFTIME('%d', 'now');

SELECT strftime('%d', order_date) AS 'order_day',
  COUNT(*) 
FROM bakery 
GROUP BY 1
ORDER BY 2 DESC;