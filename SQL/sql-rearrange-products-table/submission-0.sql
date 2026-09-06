-- Write your query below
with stores as (
    select 'store1' as store
    union all
    select 'store2' as store
    union all
    select 'store3' as store
)
select * 
from (
    select 
        product_id, 
        s.store,
        case 
            when p.store1 is not null and s.store = 'store1' then p.store1 
            when p.store2 is not null and s.store = 'store2' then p.store2
            when p.store3 is not null and s.store = 'store3' then p.store3
            else null
        end
        as price
    from products p
        left join stores s on 1=1
)
where price is not null