SELECT DATETIME(timestring, modifier1, modifier2, ...);
SELECT DATE('2005-09-15', 'start of month');
SELECT DATETIME('2020-02-10', 'start of month', '-1 day', '+7 hours');

SELECT DATETIME(order_date, 'start of day', '+2 days', '+7 hours')
FROM bakery;