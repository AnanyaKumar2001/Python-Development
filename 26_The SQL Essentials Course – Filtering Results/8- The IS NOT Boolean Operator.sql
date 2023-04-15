-- *-*-*-*-*-*-*-*-*- The IS NOT Boolean Operator *-*-*-*-*-*-*-*-*-

USE helalee_db; 

-- Example 32
SELECT e.first_name, e.last_name, e.phone_number
FROM employees e
WHERE 
e.phone_number IS NOT NULL;
-- ------------------------------
