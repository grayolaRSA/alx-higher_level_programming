-- script creates table
-- if table exists already script not to fail
-- database name passed as argument
CREATE TABLE IF NOT EXISTS unique_id (
id INT DEFAULT 1,
name VARCHAR(256));
