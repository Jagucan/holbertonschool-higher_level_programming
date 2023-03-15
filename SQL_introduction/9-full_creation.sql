-- Full creation 

CREATE TABLE IF NOT EXISTS second_table(
    id INT, 
    name VARCHAR(256),
    score INT,
    PRIMARY KEY (id)
);

ALTER TABLE second_table MODIFY COLUMN id INT AUTO_INCREMENT;

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
