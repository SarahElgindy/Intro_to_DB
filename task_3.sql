-- List all the tables in the specified database
SELECT table_name 
FROM INFORMATION_SCHEMA.tables 
WHERE table_schema = 'alx_book_store';
