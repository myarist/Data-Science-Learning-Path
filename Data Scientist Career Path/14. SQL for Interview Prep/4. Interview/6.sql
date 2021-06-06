SELECT *
FROM projects
LEFT JOIN employees
  ON projects.employee_id = employees.id;