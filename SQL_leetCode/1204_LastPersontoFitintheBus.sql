-- Write your PostgreSQL query statement below
with t as (
    select
        person_name,
        sum(Weight) over (order by Turn) as total
    from Queue
)

select person_name
from t
where total <= 1000
order by total desc
limit 1;
