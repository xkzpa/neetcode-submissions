-- Write your query below
select 
    u.name, 
    sum(amount) as balance
from transactions t
    right join users u on t.account = u.account
group by 1
having sum(amount) > 10000