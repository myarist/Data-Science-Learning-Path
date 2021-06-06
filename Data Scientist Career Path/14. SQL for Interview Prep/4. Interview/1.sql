SELECT title, author, average_rating
FROM books 
WHERE average_rating
BETWEEN 3.5 AND 4.5;

SELECT DISTINCT author
FROM books;