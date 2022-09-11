-- change the encoding of database, table and field
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- convert table 'first_table'
USE hbtn_0c_0;
ALTER TABLE first_table
COLLATE utf8mb4_unicode_ci;

-- convert field 'name' in 'first_table'
ALTER TABLE first_table
CHANGE name name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
