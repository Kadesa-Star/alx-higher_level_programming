-- List all records with a name value from second_table, display score and name, and ordering by descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
