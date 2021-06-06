SELECT *
FROM classes
JOIN students
  ON classes.id = students.class_id;