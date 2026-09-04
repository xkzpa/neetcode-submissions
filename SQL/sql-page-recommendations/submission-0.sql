
select
    distinct page_id as recommended_page
from likes 
where user_id in (
    select distinct
        coalesce(
            case when user1_id = 1 then null else user1_id end, 
            case when user2_id = 1 then null else user2_id end
        )
    from friendship
    where user1_id = 1 or user2_id = 1
)
and page_id not in (select distinct page_id from likes where user_id = 1)
order by 1