-- Write your query below
with enhanced as (
    select
        *,
        case 
            when from_id > to_id then to_id || '|' ||from_id
            else from_id || '|' || to_id
        end
    connection_id
    from calls
)
select
    min(split_part(connection_id, '|', 1)) as person1,
    min(split_part(connection_id, '|', 2)) as person2,
    count(*) as call_count, sum(duration) as total_duration
from enhanced
group by connection_id