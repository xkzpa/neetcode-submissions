-- Write your query below
with counted as (
    select
        order_date = customer_pref_delivery_date as is_immediate, 
        count(*) as cnt
    from delivery
    group by 1
),
all_cnt as (
    select count(*) cntg from delivery
)
select 
    round(coalesce(cnt, 0) * 100.0 / cntg, 2)  as immediate_percentage
from all_cnt left join counted on is_immediate = true 

