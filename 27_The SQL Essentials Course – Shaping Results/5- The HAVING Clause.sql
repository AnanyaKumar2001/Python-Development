-- *-*-*-*-*-*-*-*-*- The HAVING Clause *-*-*-*-*-*-*-*-*-

USE helalee_db; 

-- Example 46
-- SELECT COUNT(l.country_id), l.country_id
-- FROM locations l
-- GROUP BY l.country_id
-- HAVING l.country_id = 'US';
-- ------------------------------



-- Example 47
-- SELECT COUNT(l.country_id), l.country_id
-- FROM locations l
-- GROUP BY l.country_id
-- HAVING l.country_id = 'UK';
-- ------------------------------


-- Example 48
-- SELECT COUNT(l.country_id), l.country_id
-- FROM locations l
-- GROUP BY l.country_id
-- HAVING COUNT(l.country_id) > 1;
-- ------------------------------


-- Example 49
SELECT COUNT(l.country_id) as countryID, l.country_id
FROM locations l
GROUP BY l.country_id
HAVING countryID >= 2;
-- ------------------------------