-- Import the table dump into the hbtn_0c_0 database
-- Display the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;

