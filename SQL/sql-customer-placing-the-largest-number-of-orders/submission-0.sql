-- Write your query below
select customer_number
from orders
group by 1
order by count(order_number) desc, customer_number
limit 1 