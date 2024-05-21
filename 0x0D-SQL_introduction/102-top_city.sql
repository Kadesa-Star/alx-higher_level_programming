-- Display the top 3 cities temps during july and august ordered temp descending
SELECT City, Temperature
FROM temperature
WHERE MONTH(Date) IN (7, 8)
ORDER BY Temperature DESC
LIMIT 3;
