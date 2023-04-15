-- *-*-*-*-*-*-*-*-*- The AND Boolean Operator *-*-*-*-*-*-*-*-*-

USE helalee_db; 

-- Example 22
SELECT e.employee_id, e.first_name, e.last_name, e.salary
FROM employees e
WHERE
e.salary > 4000
AND
e.salary < 10000;
-- ------------------------------
