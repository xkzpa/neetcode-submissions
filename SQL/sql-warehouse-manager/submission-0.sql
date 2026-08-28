-- Write your query below
with product_dim as (
    select
        product_id, width * length * height as pr_volume
    from products
)
select
    w.name as warehouse_name,
    sum(p.pr_volume * units ) as volume
from warehouse w
left join product_dim as p on w.product_id = p.product_id
group by 1