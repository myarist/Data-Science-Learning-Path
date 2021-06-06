WITH play_count AS (
   SELECT song_id,
      COUNT(*) AS 'times_played'
   FROM plays
   GROUP BY song_id)
SELECT songs.title,
  songs.artist,
  play_count.times_played
FROM play_count
JOIN songs
  ON play_count.song_id = songs.id;