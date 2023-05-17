-- script lists cities that can be found in database
-- joins two tables
-- Script that lists all the cities of California registered in the database
SELECT id, name
FROM cities
WHERE state_id = (
      SELECT id
      FROM states
      WHERE name = "California");
