DROP TABLE lightsabers;
DROP TABLE characters;

CREATE TABLE characters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    darkside BOOLEAN,
    age INT
);

CREATE TABLE lightsabers (
    id SERIAL PRIMARY KEY,
    hilt_metal VARCHAR(255) NOT NULL,
    colour VARCHAR(255) NOT NULL,
    character_id INT REFERENCES characters(id)
);

INSERT INTO characters(name, darkside, age) VALUES('Obi-Wan Kenobi', false, 27);
INSERT INTO characters(name, darkside, age) VALUES('Anakin Skywalker', false, 19);
INSERT INTO characters(name, darkside, age) VALUES('Darth Maul', true, 32);

INSERT INTO characters(name, darkside) VALUES('Yoda', false);
INSERT INTO characters(name, darkside, age) VALUES('Luke Skywalker', false, 17);
INSERT INTO characters(name, darkside, age) VALUES('Qui Gon Jin', false, 45);

INSERT INTO characters(name, darkside, age) VALUES('Stormtrooper', true, 25);
INSERT INTO characters(name, darkside, age) VALUES('Stormtrooper', true, 25);
INSERT INTO characters(name, darkside, age) VALUES('Stormtrooper', true, 25);
INSERT INTO characters(name, darkside, age) VALUES('Stormtrooper', true, 25);
INSERT INTO characters(name, darkside, age) VALUES('Stormtrooper', true, 25);


INSERT INTO lightsabers(hilt_metal, colour, character_id) VALUES('gold', 'red', 2);
INSERT INTO lightsabers(hilt_metal, colour, character_id) VALUES('palladium', 'green', 4);
INSERT INTO lightsabers(hilt_metal, colour, character_id) VALUES('tungsten', 'brown', 1);
-- INSERT INTO lightsabers(colour) VALUES('red');

UPDATE lightsabers SET ID = 1;



UPDATE characters SET age = 29 WHERE id = 9;

-- SELECT COUNT(*) FROM characters;

-- UPDATE characters SET darkside = true;

UPDATE characters SET darkside = true WHERE name = 'Anakin Skywalker';

UPDATE characters SET age = 65 WHERE name = 'Obi-Wan Kenobi';

DELETE FROM characters WHERE name = 'Darth Maul';
DELETE FROM characters WHERE name = 'Qui Gon Jin';




SELECT * FROM characters;
SELECT * FROM lightsabers;