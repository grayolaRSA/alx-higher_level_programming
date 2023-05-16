-- list all tables in MYSQL server
-- mysql used as example name of server
SET @dbname = 'mysql';
SELECT table_name FROM information_schema.tables WHERE table_schema = @dbname;
