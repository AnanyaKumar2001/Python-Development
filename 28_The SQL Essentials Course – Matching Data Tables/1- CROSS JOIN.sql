-- *-*-*-*-*-*-*-*-*- CROSS JOIN *-*-*-*-*-*-*-*-*-

USE helalee_db; 

-- Example 50
SELECT 
e.first_name,
e.last_name,
d.department_name
FROM
employees e,
departments d;
-- ------------------------------