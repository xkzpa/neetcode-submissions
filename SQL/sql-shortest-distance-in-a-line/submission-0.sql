-- Write your query below
select min(distance) as shortest
from (
    select x - lag(x) over (order by x) as distance
    from point
)
