CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;

CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15),
    course VARCHAR(50) NOT NULL,
    semester INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Example SELECT query:
SELECT * FROM students;

-- Example INSERT query (change the email if this sample is run more than once):
-- INSERT INTO students (first_name, last_name, email, phone, course, semester)
-- VALUES ('Asha', 'Kumar', 'asha.example@example.com', '9876543210', 'BCA', 2);
