
SELECT first_name, last_name
FROM  actor
where actor_id in (
		select actor_id 
		from film_actor
		WHERE film_id in (
			SELECT film_id FROM film
			WHERE title = 'ALTER VICTORY'
		)
	)
	
SELECT count(*)
from film
where film_id in (
	SELECT film_id
	FROM inventory 
	where inventory_id in (
			select inventory_id 
			from rental
			WHERE staff_id in (
				SELECT staff_id FROM staff
				WHERE first_name = 'Jon' AND last_name = 'Stephens'
			)
		)
	)
	

