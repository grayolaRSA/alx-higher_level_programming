-- script creates table
-- if table exists already script not to fail
-- database name passed as argument
CREATE TABLE IF NOT EXISTS id_not_null (
id INT DEFAULT 1,
name VARCHAR(256));
