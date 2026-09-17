-- Write your query below
select distinct player_id, device_id
from (
    select player_id, device_id, row_number() over (partition by player_id order by event_date) as rn
    from activity
)
where rn = 1