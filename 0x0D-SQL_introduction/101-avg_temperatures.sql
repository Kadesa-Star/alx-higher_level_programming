-- Display average temp (Fahrenheit) by city ordered by temp (descending)
SELECT City, AVG(Temperature) AS Average_Temperature_Fahrenheit
FROM temperatures
GROUP BY City
ORDER BY Average_Temperature_Fahrenheit DESC;

