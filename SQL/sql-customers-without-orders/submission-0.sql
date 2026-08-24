-- Write your query below
select distinct c.name
from customers c
left join orders o on o.customer_id = c.id
where o.id is null
