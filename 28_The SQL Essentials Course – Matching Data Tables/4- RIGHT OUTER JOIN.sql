-- *-*-*-*-*-*-*-*-*- RIGHT OUTER JOIN *-*-*-*-*-*-*-*-*-

USE helalee_db; 

-- Example 54
SELECT
e.first_name,
e.last_name,
d.department_name,
d.department_id
FROM 
employees e
RIGHT OUTER JOIN
departments d
ON
e.department_id = d.department_id;
-- ------------------------------