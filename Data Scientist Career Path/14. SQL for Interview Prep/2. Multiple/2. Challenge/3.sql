SELECT users.id
FROM users
LEFT JOIN premium_users
  ON users.id = premium_users.user_id
WHERE premium_users.user_id IS NULL;