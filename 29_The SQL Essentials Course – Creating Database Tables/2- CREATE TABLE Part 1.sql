-- *-*-*-*-*-*-*-*-*- CREATE TABLE Part 1 *-*-*-*-*-*-*-*-*-
/*
*-*-*-*-*---------------******************--------------------------------- Standard SQL Data Types
	Data Type					Value Space
	1- CHARACTER				can hold N character values - set N to statically
	2- CHARACTER VARYING		can hold N character values - set N to dynamically - storage can be less that N
	3- BINARY					hexadecimal data
	4- SMALLINT					-2^15 (-32768) to 2^15 (32768)
	5- INTEGER					-2^31 (-2,147,483,648) to 2^31-1 (2,147,483,647)
	6- BIGINT					-2^63 (-9,223,372,036,854,775,808) to 2^63-1 (9,223,372,036,854,775,807)
	7- BOOLEAN					TRUE or FALSE
	8- DATE						YEAR, MONTH, & DAY in the format YYYY-MM-DD
	9- TIME						HOUR, MINUTE & SECOND in the format HH:MM:SS[.sF] where F is the fractional part of the second
	10- TIMESTAMP				Both DATE & TIME
*/

-- Example 56
USE sql_course;

CREATE TABLE students 
(
student_id INTEGER,
first_name VARCHAR(255),
last_name VARCHAR(255)
);
-- ----------------------------
