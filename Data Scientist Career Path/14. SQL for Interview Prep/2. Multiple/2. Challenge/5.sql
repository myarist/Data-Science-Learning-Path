SELECT premium_users.user_id,
	premium_users.purchase_date,
  premium_users.cancel_date,
  months.months
FROM premium_users
CROSS JOIN months;
