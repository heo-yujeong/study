DROP TABLE zoo;
CREATE TABLE zoo (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name Text,
  eat Text,
  weight INTEGER,
  height INTEGER,
  age INTEGER
);

INSERT INTO zoo (name, eat, weight, height, age)
VALUES ('Lion', 'Meat', 200, 120, 5),
       ('Elephant', 'Plants', 5000, 300, 15),
       ('Giraffe', 'Leaves', 1500, 550, 10),
       ('Monkey', 'Fruits', 50, 60, 8);

ALTER TABLE zoo
ADD COLUMN species Text;

UPDATE zoo
SET species = 'Panthera leo'
WHERE name = 'Lion';
UPDATE zoo
SET species = 'Loxodonta africana'
WHERE name = 'Elephant';
UPDATE zoo
SET species = 'Giraffa camelopardalis'
WHERE name = 'Giraffe';
UPDATE zoo
SET species = 'Cebus capucinus'
WHERE name = 'Monkey';

UPDATE zoo
SET height = height * 2.54;

SELECT *
FROM zoo;