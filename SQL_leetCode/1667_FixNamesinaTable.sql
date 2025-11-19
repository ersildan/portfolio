SELECT 
    user_id,
    CASE
        WHEN array_length(string_to_array(name, ' '), 1) = 2 
        THEN CONCAT(
            INITCAP((string_to_array(name, ' '))[1]),
            ' ',
            LOWER((string_to_array(name, ' '))[2])
        )
        ELSE INITCAP(name)
    END as name
FROM Users
ORDER BY user_id;


-- SELECT 
--     user_id,
--     UPPER(SUBSTRING(name FROM 1 FOR 1)) || LOWER(SUBSTRING(name FROM 2)) as name
-- FROM Users
-- ORDER BY user_id;