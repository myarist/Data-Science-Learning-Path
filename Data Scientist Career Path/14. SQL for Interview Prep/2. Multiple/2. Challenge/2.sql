 SELECT plays.user_id,
   plays.play_date,
   songs.title
FROM plays
JOIN songs
  ON plays.song_id = songs.id;