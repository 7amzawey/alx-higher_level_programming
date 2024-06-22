-- this script lists all the cities of california
SELECT cities.id, cities.name FROM cities, states
WHERE states.id = cities.state_id
AND states.name = 'California'
ORDER BY cities.id ASC;
