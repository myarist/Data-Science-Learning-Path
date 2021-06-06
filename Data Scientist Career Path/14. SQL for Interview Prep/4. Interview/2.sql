SELECT id, 
  CASE
    WHEN home_points > away_points 
      THEN 'HOME WIN'
    ELSE 'AWAY WIN'
  END
FROM nba_matches;