-- Write your query below
with spends_by_months as (
    select
        o.customer_id,         
        date_trunc('month', order_date)::date as order_month,
        sum(quantity * p.price) as month_spend        
    from orders o
        left join product p on p.product_id = o.product_id
        left join customers c on c.customer_id = o.customer_id
    group by 1,2    
)
select 
    distinct c.customer_id, c.name
from customers c 
    right join spends_by_months s1 on c.customer_id = s1.customer_id and s1.order_month = '2020-06-01'
    right join spends_by_months s2 on c.customer_id = s2.customer_id and s2.order_month = '2020-07-01'
where s1.month_spend >= 100 and s2.month_spend >= 100
