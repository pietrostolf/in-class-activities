CREATE VIEW title_count_join
as
select f.title
, count(i.inventory_id) as "num_copies"
from film as f
join inventory as i
on i.film_id = f.film_id
GROUP by f.title
order by "num_copies" desc

CREATE VIEW title_count_no_join
as
select title 
, (SELECT count(i.film_id) from inventory as i where f.film_id = i.film_id) as "num_copies"
from film f
order by title asc

SELECT title, num_copies
FROM public.title_count_join
where "num_copies" = 7
order by title asc
	
	
SELECT title, num_copies
FROM public.title_count_no_join
where "num_copies" = 7
order by title asc