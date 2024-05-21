-- Convert the entire database hbtn_0c_0 to UTF8.
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the first_table table to UTF-8
ALTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
