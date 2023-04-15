-- *-*-*-*-*-*-*-*-*- The OR Boolean Operator *-*-*-*-*-*-*-*-*-

USE helalee_db; 

-- Example 23
SELECT e.first_name, e.last_name, e.email, e.salary
FROM employees e
WHERE
e.salary < 5000
OR
e.salary > 15000
-- ------------------------------
