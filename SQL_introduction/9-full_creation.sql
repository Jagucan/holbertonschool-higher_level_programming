-- Full creation 

CREATE TABLE IF NOT EXISTS second_table(
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256),
    score INT,
    PRIMARY KEY (id)
);

INSERT INTO  second_table (name, score) VALUES(
    'Jhon',
    '10'
);

INSERT INTO  second_table (name, score) VALUES(
    'Alex',
    '3'
);

INSERT INTO  second_table (name, score) VALUES(
    'Bob',
    '14'
);

INSERT INTO  second_table (name, score) VALUES(
    'George',
    '8'
);
