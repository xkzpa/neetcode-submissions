-- Write your query below
select distinct li1.account_id
from log_info li1
    join log_info li2 on li1.account_id = li2.account_id
        and
            (
                li1.login between li2.login and li2.logout
                or li2.login between li1.login and li1.logout
            )
        and li1.ip_address != li2.ip_address
order by 1