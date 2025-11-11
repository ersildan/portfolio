WITH temp AS (
    SELECT
        id, num,
        id - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) as rn_dif
    FROM logs
)

select DISTINCT num AS ConsecutiveNums
from temp
group by num, rn_dif
HAVING COUNT(*) >= 3;

-- SELECT DISTINCT num AS ConsecutiveNums
-- FROM logs
-- GROUP BY num, id - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id)
-- HAVING COUNT(*) >= 3
