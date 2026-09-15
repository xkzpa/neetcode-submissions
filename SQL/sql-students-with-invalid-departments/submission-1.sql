-- Write your query below
select id, name
from students where department_id not in (select id from departments)  or department_id is null