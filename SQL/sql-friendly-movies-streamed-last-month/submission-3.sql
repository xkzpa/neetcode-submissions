-- Write your query below
select distinct title
from content c
    right join tv_program tv 
    on c.content_id = tv.content_id
where kids_content = 'Y'
and date_trunc('month', program_date::date) = '2020-06-01'
and content_type = 'Movies'

