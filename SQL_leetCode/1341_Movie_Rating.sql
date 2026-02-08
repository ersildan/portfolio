-- Write your PostgreSQL query statement below
(select
    u.name as results
from Users u
join MovieRating m using(user_id)
group by name
order by COUNT(*) DESC, name ASC
limit 1)

union all

(select
    mov.title as results
from Movies mov
join MovieRating m using(movie_id)
where m.created_at BETWEEN '2020-02-01' AND '2020-02-29'
group by title
order by (avg(m.rating)) DESC, title
limit 1)