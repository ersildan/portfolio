delete from Person
where id not in
     (select min(id) 
     from Person
     group by email);


DELETE FROM Person 
WHERE id IN (
    SELECT id FROM (
        SELECT id, 
               ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) as rn
        FROM Person
    ) t WHERE rn > 1
);