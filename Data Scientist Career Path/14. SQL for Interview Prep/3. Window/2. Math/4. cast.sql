SELECT CAST(3 AS REAL) / 2; -- 1.5
SELECT CAST('3.14 is pi' AS REAL);

SELECT item_name, (price - CAST(discount AS REAL)) * quantity
FROM bakery;