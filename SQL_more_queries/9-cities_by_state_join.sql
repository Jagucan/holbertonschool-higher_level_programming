-- lists all cities contained in the database - Cities by States 
SELECT cities.id, cities.name, states.name AS name FROM cities JOIN states ON cities.state_id = states.id;