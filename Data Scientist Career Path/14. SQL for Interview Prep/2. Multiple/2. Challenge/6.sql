SELECT premium_users.user_id,
  months.months,
  CASE
    WHEN (
      premium_users.purchase_date <=
             months.months
      )
      AND
      (
        (premium_users.cancel_date >=
                months.months)
        OR
        premium_users.cancel_date IS NULL
      )
    THEN 'active'
    ELSE 'not_active'
  END as status

FROM premium_users
CROSS JOIN months;
