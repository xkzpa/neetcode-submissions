-- Write your query below
with calls_groupped as (
    select 
        GREATEST(caller_id, callee_id),
        LEAST(caller_id, callee_id),
        sum(duration) as call_duration,
        min(left(p1.phone_number, 3)) cc1,
        min(left(p2.phone_number, 3)) cc2
    from calls c
        left join person p1 on c.caller_id = p1.id
        left join person p2 on c.callee_id = p2.id
    group by 1,2
)
,globalc as (
    select 
        c.name,
        sum(call_duration) as call_duration
    from calls_groupped cg
    left join country c on cg.cc1 = c.country_code or cg.cc2 = c.country_code
    group by 1
)
select name as country
from globalc
where call_duration > (select avg(call_duration) from globalc)