-- Write your query below

with root as (
    select id, 'Root' as type
    from tree
    where p_id is null
)
, parents as (
    select distinct id, 'Inner'
    from tree 
    where id in (select distinct p_id from tree)  and id not in (select id from root)
)
, no_childs as (
    select id, 'Leaf'
    from tree
    where id not in (select id from parents) and id not in (select id from root)
)

select * from root
union all 
select * from parents
union all 
select * from no_childs