-- Lists all records of table `second_table`
SELECT score, name
FROM second_table
WHERE name NOT IN ('')
ORDER BY score DESC;
