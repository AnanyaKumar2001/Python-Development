-- *-*-*-*-*-*-*-*-*- The UPDATE Statement *-*-*-*-*-*-*-*-*-

USE helalee_db;


-- Example 11 ->>>> Updating a single record
-- UPDATE departments
-- SET department_name = 'Web Development', location_id = 9009
-- WHERE department_id = 1;
-- -----------------------------




-- Example 12 ->>>> Updating multiple records
-- UPDATE locations
-- SET city = 'Kabul'
-- WHERE country_id = 'US';
-- -----------------------------




-- Example 13 ->>>> Updating all records
UPDATE locations
SET city = 'Herat';
-- -----------------------------