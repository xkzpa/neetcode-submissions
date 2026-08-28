-- Write your query below
select 
    teams.team_id, teams.team_name, coalesce(res.num_points, 0) as num_points
from (
    select 
        team_id, sum(points) as num_points
    from 
    (
        select 
            host_team as team_id, 
            match_id,
            case 
                when host_goals - guest_goals > 0 then 3
                when host_goals - guest_goals < 0 then 0
                else 1
            end as points
        from matches

        union all

        select 
            guest_team, 
            match_id,
            case 
                when guest_goals - host_goals > 0 then 3
                when guest_goals - host_goals < 0 then 0
                else 1
            end as points
        from matches
    )
    group by 1
) as res
full outer join teams on res.team_id = teams.team_id
order by 3 desc, res.team_id