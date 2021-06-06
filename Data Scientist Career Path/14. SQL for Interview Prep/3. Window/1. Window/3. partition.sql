SELECT 
    username,
    month,
    change_in_followers,
    SUM(change_in_followers) OVER (
      PARTITION BY username 
      ORDER BY month
    ) 'running_total_followers_change',
    AVG(change_in_followers) OVER (
      PARTITION BY username 
      ORDER BY month
    ) 'running_avg_followers_change'
FROM
    social_media;