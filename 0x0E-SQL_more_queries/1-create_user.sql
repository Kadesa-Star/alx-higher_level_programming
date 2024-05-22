-- Creates the MySQL server user user_0d_1 and grants all privileges
GRANT ALL PRIVILEGES
        ON *.*
        TO 'user_0d_1'@'localhost'
        IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;
