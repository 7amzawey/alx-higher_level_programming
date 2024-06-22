-- list all cities contained in the database hbtn_0d_usa
select cities.id, cities.name, states.name from states, cities
order by cities.id asc;
