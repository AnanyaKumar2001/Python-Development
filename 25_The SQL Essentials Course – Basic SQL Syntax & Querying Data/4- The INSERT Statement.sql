-- *-*-*-*-*-*-*-*-*- The INSERT Statement *-*-*-*-*-*-*-*-*-

USE helalee_db;


-- Example 8 ---->>>> Approach One - Adding a Single Record
-- INSERT INTO countries
-- VALUES ('AF', 'Afghanistan', 1001);
-- -----------------------------



-- Example 9 ---->>>> Approach Two - Adding a Single Record
-- INSERT INTO countries (country_id, country_name, region_id)
-- VALUES ('NZ', 'New Zealand', 9009);
-- -----------------------------




-- Example 10 ---->>>> Approach Two - Adding a Single Record
INSERT INTO countries (country_id, country_name, region_id)
VALUES ('JT', 'Jupyter', 2002);

INSERT INTO countries (country_id, country_name, region_id)
VALUES ('MZ', 'Mars', 3003);
-- -----------------------------
