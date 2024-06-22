-- list all cities contained in the database hbtn_0d_usa
select cities.id, cities.name, states.name as state_name from cities
INNER JOIN states ON cities.state_id = states.id
order by cities.id asc;
