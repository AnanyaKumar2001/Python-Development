-- *-*-*-*-*-*-*-*-*- CREATE TABLE Part 2 *-*-*-*-*-*-*-*-*-

USE sql_course;

-- Example 62 ->>>> NOT RECOMMENDED
/*
CREATE TABLE students
(
student_id INTEGER NOT NULL PRIMARY KEY,
first_name VARCHAR(255),
last_name VARCHAR(255)
);

CREATE TABLE email_address
(
email_address_id INTEGER NOT NULL PRIMARY KEY,
email_address VARCHAR(255),
email_address_student_id INTEGER,

CONSTRAINT 
FK_email_address_student_id
FOREIGN KEY
(email_address_student_id)
REFERENCES
students
(student_id)
);
*/
-- ----------------------------




-- Example 63 ->>>> RECOMMENDED

CREATE TABLE students
(
student_id INTEGER NOT NULL PRIMARY KEY,
first_name VARCHAR(255),
last_name VARCHAR(255)
);


CREATE TABLE email_address
(
email_address_id INTEGER NOT NULL PRIMARY KEY,
email_address VARCHAR(255),
email_address_student_id INTEGER
);


ALTER TABLE
email_address
ADD CONSTRAINT
FK_email_address_student_id
FOREIGN KEY
(email_address_student_id)
REFERENCES
students
(student_id);

-- DROP TABLE students;
-- DROP TABLE email_address;