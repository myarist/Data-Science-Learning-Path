SELECT title, week, gross, 
  SUM(gross) OVER (
    PARTITION BY title 
    ORDER BY week
  ) AS 'running_total_gross'
FROM box_office;