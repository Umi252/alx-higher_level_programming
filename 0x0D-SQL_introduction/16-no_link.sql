-- Lists all records of the table second_table having a name value in my MySQL server.
-- Records are ordered by descending score.
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
