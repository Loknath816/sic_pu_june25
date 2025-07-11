create database nithin_db;
use nithin_db;
CREATE TABLE employee (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    designation VARCHAR(30),
    phone_number BIGINT UNIQUE,
    salary FLOAT,
    commission FLOAT DEFAULT 0,
    years_of_experience TINYINT,
    technology VARCHAR(30) NOT NULL
);

INSERT INTO employee VALUES (1, 'Aarav Mehta', 'Developer', 9123456780, 65000, 5000, 4, 'Java');
INSERT INTO employee VALUES (2, 'Diya Rao', 'Analyst', 9123456781, 58000, 3000, 3, 'Python');
INSERT INTO employee VALUES (3, 'Rohan Kulkarni', 'Tester', 9123456782, 48000, 2500, 2, 'Selenium');
INSERT INTO employee VALUES (4, 'Sneha Iyer', 'Manager', 9123456783, 85000, 10000, 8, 'Agile');
INSERT INTO employee VALUES (5, 'Vikram Shah', 'Lead Developer', 9123456784, 90000, 7000, 6, 'Node.js');
INSERT INTO employee (id, name, phone_number, salary, years_of_experience, technology)
VALUES (6, 'Meera Jain', 9123456785, 55000, 4, 'React');

INSERT INTO employee (id, name, designation, phone_number, salary, technology)
VALUES (7, 'Karan Verma', 'Support Engineer', 9123456786, 40000, 'MySQL');

INSERT INTO employee (id, name, designation, phone_number, salary, commission, technology)
VALUES (8, 'Pooja Das', 'Consultant', 9123456787, 72000, 5000, 'AWS');

INSERT INTO employee (id, name, phone_number, salary, commission, technology)
VALUES (9, 'Amit Tiwari', 9123456788, 60000, 4000, 'DevOps');

INSERT INTO employee (id, name, designation, phone_number, years_of_experience, technology)
VALUES (10, 'Ritika Sen', 'Designer', 9123456789, 2, 'UI/UX');

INSERT INTO employee (id, name, phone_number, technology)
VALUES (11, 'Ishan Choudhary', 9123456790, 'JavaScript');

INSERT INTO employee (id, name, phone_number, technology)
VALUES (12, 'Neha Kapoor', 9123456791, 'HTML');

INSERT INTO employee (id, name, phone_number, technology)
VALUES (13, 'Rahul Sinha', 9123456792, 'C++');

INSERT INTO employee (id, name, phone_number, technology)
VALUES (14, 'Anjali Batra', 9123456793, 'Swift');

INSERT INTO employee (id, name, phone_number, technology)
VALUES (15, 'Mohit Yadav', 9123456794, 'Kotlin');
INSERT INTO employee VALUES (16, 'Zara Hussain', 'Product Owner', 9123456795, 94000, 12000, 9, 'Scrum');

INSERT INTO employee (id, name, phone_number, technology)
VALUES (17, 'Sunny Ahuja', 9123456796, 'PHP');

INSERT INTO employee (id, name, designation, phone_number, salary, technology)
VALUES (18, 'Kabir Nanda', 'Data Scientist', 9123456797, 110000, 'ML');

INSERT INTO employee (id, name, designation, phone_number, salary, commission, years_of_experience, technology)
VALUES (19, 'Tara Bose', 'DBA', 9123456798, 75000, 5000, 5, 'Oracle');

INSERT INTO employee (id, name, phone_number, salary, years_of_experience, technology)
VALUES (20, 'Devansh Patel', 9123456799, 67000, 4, 'Azure');



