-- *-*-*-*-*-*-*-*-*- Set Functions *-*-*-*-*-*-*-*-*-

USE helalee_db; 

/* Set Functions
COUNT()
MAX()
MIN()
AVG()
SUM()
*/

-- Example 36 ->>>> COUNT()
-- SELECT COUNT(*)
-- FROM employees;
-- ------------------------------



-- Example 37 ->>>> COUNT()
-- SELECT COUNT(e.phone_number)
-- FROM employees e;
-- ------------------------------



-- Example 38 ->>>> COUNT()
-- SELECT COUNT(e.first_name), e.salary
-- FROM employees e
-- WHERE
-- e.salary > 10000;
-- ------------------------------


-- Example 39 ->>>> MAX()
-- SELECT MAX(e.salary)
-- FROM employees e;
-- ------------------------------



-- Example 40 ->>>> MIN()
-- SELECT MIN(e.salary)
-- FROM employees e;
-- ------------------------------



-- Example 41 ->>>> AVG()
-- SELECT AVG(e.salary)
-- FROM employees e;
-- ------------------------------



-- Example 42 ->>>> ROUND(AVG())
-- SELECT ROUND(AVG(e.salary))
-- FROM employees e;
-- ------------------------------



-- Example 43 ->>>> SUM()
SELECT SUM(e.salary)
FROM employees e;
-- ------------------------------

