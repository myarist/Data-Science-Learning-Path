SELECT grade
FROM math_students
WHERE EXISTS (
  SELECT grade
  FROM english_students
);