-- This script lists all the tables in the given database using the SHOW TABLES command.
SELECT table_name 
FROM INFORMATION_SCHEMA.tables 
WHERE table_schema = USE alx_book_store;
