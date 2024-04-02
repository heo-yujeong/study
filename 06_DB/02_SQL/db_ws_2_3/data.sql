SELECT *
FROM hotels;

UPDATE hotels
SET grade = UPPER(grade);

SELECT grade
FROM hotels;

CREATE TABLE customers (
  id INTEGER PRIMARY KEY,
  name Text,
  email Text
);

CREATE TABLE reservations (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  room_num Text,
  check_in Text,
  check_out Text,
  FOREIGN KEY(customer_id) REFERENCES customers(id),
  FOREIGN KEY(room_num) REFERENCES hotels(room_num)
);

INSERT INTO customers
VALUES (1, '홍길동', 'john@example.com'),
       (2, '박지영', 'jane@example.com'),
       (3, '김미영', 'alice@example.com'),
       (4, '이철수', 'bob@example.com');

INSERT INTO reservations
VALUES (1, 1, 101, '2024-03-20', '2024-03-25'),
       (2, 2, 202, '2024-03-21', '2024-03-24'),
       (3, 3, 303, '2024-03-22', '2024-03-26'),
       (4, 4, 404, '2024-03-23', '2024-03-27');

SELECT * FROM customers;
SELECT * FROM reservations;