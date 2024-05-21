-- Import the table dump int the specified database
SOURCE /path/to/table_dump.sql;
-- Display the max temperature of each state ordered by state name
SELECT State, MAX(Temperature) AS Max_Temperature
FROM temperature
GROUP BY State
ORDER BY State;
