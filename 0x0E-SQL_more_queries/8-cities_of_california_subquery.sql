-- script lists cities that can be found in database
-- joins two tables
USE hbtn_0d_usa;
SELECT cities.name, states.name
FROM cities, states
WHERE states.name = "California"
AND cities.state_id = states.id
ORDER BY cities.id;
