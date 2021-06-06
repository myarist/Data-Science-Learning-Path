SELECT category, SUM(downloads)
FROM fake_apps
GROUP BY category;