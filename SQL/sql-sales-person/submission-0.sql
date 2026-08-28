-- Write your query below
select name
from sales_person where sales_id not in (
    select sales_id
    from orders o
    join company c on o.com_id = c.com_id
    where c.name = 'CRIMSON'
)

