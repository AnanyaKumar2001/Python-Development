-- *-*-*-*-*-*-*-*-*- The IN Boolean Operator *-*-*-*-*-*-*-*-*-

USE helalee_db; 

-- Example 30
SELECT e.first_name, e.last_name, e.hire_date
FROM employees e
WHERE e.manager_id
IN (100, 103, 108);
-- ------------------------------
