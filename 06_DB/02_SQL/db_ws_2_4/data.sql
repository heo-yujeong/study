CREATE TABLE transactions (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  amount Text,
  transaction_date Date,
  FOREIGN KEY(user_id) REFERENCES users(id)
);

INSERT INTO transactions
VALUES (1, 1, 500, '2024-03-15'),
       (2, 2, 700, '2024-03-16'),
       (3, 1, 200, '2024-03-17'),
       (4, 3, 1000, '2024-03-18');

SELECT first_name, last_name, amount, transaction_date
FROM users INNER JOIN transactions
ON users.id = transactions.user_id;


SELECT first_name, last_name, amount, transaction_date
FROM users INNER JOIN transactions
ON users.id = transactions.user_id
WHERE transaction_date > '2024-03-16'
GROUP BY users.id;

SELECT first_name, last_name, SUM(amount) AS total_amount
FROM users INNER JOIN transactions
ON users.id = transactions.user_id
GROUP BY users.id;