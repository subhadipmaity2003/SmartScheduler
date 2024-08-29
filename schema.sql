-- File: database/schema.sql
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  due_date DATE NOT NULL
);

INSERT INTO tasks (name, due_date) VALUES
('Task 1', '2024-09-01'),
('Task 2', '2024-09-10');
