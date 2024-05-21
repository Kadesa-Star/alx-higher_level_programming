-- Import the table dump into the hbtn_0c_0 database
SOURCE /path/to/table_dump.sql;

-- Display the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT City, AVG(Temperature) AS Average_Temperature_Fahrenheit
FROM temperatures
GROUP BY City
ORDER BY Average_Temperature_Fahrenheit DESC;

