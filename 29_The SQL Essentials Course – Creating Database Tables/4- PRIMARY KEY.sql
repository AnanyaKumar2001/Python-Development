-- *-*-*-*-*-*-*-*-*- PRIMARY KEY *-*-*-*-*-*-*-*-*-


-- Example 58
USE sql_course;

CREATE TABLE students 
(
student_id INTEGER PRIMARY KEY,
first_name VARCHAR(255) NOT NULL,
last_name VARCHAR(255) NOT NULL
);
-- ----------------------------
