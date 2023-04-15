-- *-*-*-*-*-*-*-*-*- The SELECT DISTINCT Statement *-*-*-*-*-*-*-*-*-

USE helalee_db;


-- Example 4
-- SELECT *
-- FROM employees;
-- -----------------------------



-- Example 5
-- SELECT department_id
-- FROM employees;
-- -----------------------------



-- Example 6
SELECT DISTINCT department_id
FROM employees;
-- -----------------------------



-- Example 7
SELECT DISTINCT first_name, last_name, manager_id
FROM employees;
-- -----------------------------




-- Example 8
SELECT DISTINCT *
FROM employees;
-- -----------------------------