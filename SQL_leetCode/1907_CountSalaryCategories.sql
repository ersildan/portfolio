-- Write your PostgreSQL query statement below
with table_ls as (
    select
        'Low Salary' as category,
        count(account_id) as accounts_count
    from Accounts
    where income < 20000
), table_as as (
    select
        'Average Salary' as category,
        count(account_id) as accounts_count
    from Accounts
    where income between 20000 and 50000
), table_hs as (
    select
        'High Salary' as category,
        count(account_id) as accounts_count
    from Accounts
    where income > 50000
)

select * from table_ls
union all
select * from table_as
union all
select * from table_hs
