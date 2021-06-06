SELECT date, (CAST(high AS 'REAL') + 
  CAST(low AS 'REAL')) / 2.0 AS 'average'
FROM weather;