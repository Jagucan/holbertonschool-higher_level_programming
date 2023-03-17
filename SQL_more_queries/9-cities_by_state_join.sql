-- lists all cities contained in the database - Cities by States 
SELECT cities.id, states.name AS name, cities.name FROM cities JOIN states ON cities.state_id = states.id;