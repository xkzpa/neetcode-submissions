-- Write your query below
select email from person group by 1 having count(*) > 1