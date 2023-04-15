-- *-*-*-*-*-*-*-*-*- The ORDER BY Clause *-*-*-*-*-*-*-*-*-

USE helalee_db; 

-- Example 33
-- SELECT e.first_name, e.last_name, e.salary
-- FROM employees e
-- ORDER BY e.salary;
-- ------------------------------



-- Example 34
-- SELECT c.country_name
-- FROM countries c
-- ORDER BY c.region_id;
-- ------------------------------



-- Example 35
SELECT c.country_name
FROM countries c
ORDER BY c.country_name;
-- ------------------------------
