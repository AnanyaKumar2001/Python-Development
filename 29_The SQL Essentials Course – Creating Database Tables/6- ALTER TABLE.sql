-- *-*-*-*-*-*-*-*-*- ALTER TABLE *-*-*-*-*-*-*-*-*-


-- Example 60

ALTER TABLE
email_address
ADD CONSTRAINT
FK_email_address_student_id
FOREIGN KEY
(email_address_student_id)
REFERENCES
students
(student_id);
-- ----------------------------
