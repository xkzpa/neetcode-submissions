-- Write your query below

with team_sizes as (
    select
        team_id, count(*) as team_size
    from employee
    group by 1
)
select employee_id, team_size
from employee e
    join team_sizes s on e.team_id = s.team_id
order by 1,2