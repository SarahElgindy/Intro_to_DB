-- task_4.sql
-- This script prints the full description of the 'books' table without using DESCRIBE or EXPLAIN.

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, COLUMN_KEY, EXTRA
FROM information_schema.columns
WHERE table_name = 'books'
AND table_schema = DATABASE();
