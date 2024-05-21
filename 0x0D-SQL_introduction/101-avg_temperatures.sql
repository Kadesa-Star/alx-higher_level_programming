-- Import the table dump into the hbtn_0c_0 database
-- Display the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT `city`, AVG(`Temperature`) AS `average_Temperature_Fahrenheit`
FROM `temperatures`
GROUP BY `city`
ORDER BY `average_Temperature_Fahrenheit` DESC;

