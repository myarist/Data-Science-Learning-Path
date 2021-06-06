WITH january AS (
  SELECT *
  FROM plays
  WHERE strftime("%m", play_date) = '01'
),
february AS (
  SELECT *
  FROM plays
  WHERE strftime("%m", play_date) = '02'

)
/*
Write query here
*/

SELECT january.user_id
FROM january
LEFT JOIN february
   ON january.user_id = february.user_id
WHERE february.user_id IS NULL;