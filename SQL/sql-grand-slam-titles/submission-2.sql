-- Write your query below
select t.player_id, min(player_name) as player_name, count(*) as grand_slams_count
from (
    select  wimbledon as player_id from championships
    union all 
    select fr_open from championships
    union all 
    select  us_open from championships
    union all 
    select  au_open from championships
) as t
 join players p on t.player_id = p.player_id
group by 1
