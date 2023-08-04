-- script that lists records that are complement of a condition
SELECT score, name FROM second_table WHERE name != '' ORDER BY score DESC;
