SELECT 
   ROW_NUMBER() OVER (
      ORDER BY streams_millions DESC
   ) AS 'row_num', 
   artist, 
   week,
   streams_millions
FROM
   streams;