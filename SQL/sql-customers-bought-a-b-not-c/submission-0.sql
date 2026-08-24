-- Write your query below

select customer_id, customer_name
from (
    select
        c.customer_id, min(customer_name) as customer_name,
        STRING_AGG(distinct o.product_name, '') as product_mix
    from customers c
        left join orders o on o.customer_id = c.customer_id and product_name in ('A', 'B', 'C')
    group by c.customer_id
)
where product_mix = 'AB'
order by customer_name