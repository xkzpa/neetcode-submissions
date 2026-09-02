-- Write your query below
select actor_id, director_id
from actor_director
group by 1,2
having count(distinct timestamp) >= 3