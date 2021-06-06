SELECT purchase_id, DATE(purchase_date, '+7 days')
FROM purchases;

SELECT STRFTIME('%H', purchase_date)
FROM purchases;