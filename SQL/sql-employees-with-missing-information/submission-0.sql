-- Write your query below
select 
    coalesce(e.employee_id, s.employee_id) as employee_id
from employees e
    full outer join salaries s on e.employee_id = s.employee_id
where name is null or salary is null
order by 1