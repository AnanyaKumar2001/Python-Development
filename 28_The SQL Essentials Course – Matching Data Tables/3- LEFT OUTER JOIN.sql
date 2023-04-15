-- *-*-*-*-*-*-*-*-*- LEFT OUTER JOIN *-*-*-*-*-*-*-*-*-

USE helalee_db; 

-- Example 52
-- SELECT
-- e.first_name,
-- e.last_name,
-- d.department_name,
-- d.department_id
-- FROM
-- employees e
-- INNER JOIN
-- departments d
-- ON
-- e.department_id = d.department_id;
-- ------------------------------



-- Example 53
SELECT
e.first_name,
e.last_name,
d.department_name,
d.department_id
FROM
employees e
LEFT OUTER JOIN
departments d
ON
e.department_id = d.department_id;
-- ------------------------------