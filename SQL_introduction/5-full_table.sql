-- Full description
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE, COLUMN_DEFAULT
FROM information_schema.columns
WHERE table_name = 'first_table' AND table_schema = 'hbtn_0c_0';
