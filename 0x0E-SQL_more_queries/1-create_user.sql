-- script creates MYSQL server user
-- grants users all rights on server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
