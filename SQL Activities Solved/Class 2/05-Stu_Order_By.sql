SELECT * FROM public.actor
ORDER BY actor_id DESC

SELECT * FROM public.film
ORDER BY film_id ASC 

SELECT first_name, COUNT(first_name) as first_name_count
from actor
GROUP BY first_name
ORDER BY first_name_count DESC


SELECT rating, AVG(rental_duration) AS avg_rental_duration
FROM film
GROUP BY rating
ORDER BY avg_rental_duration ASC;

SELECT * FROM public.film
ORDER BY length ASC 

SELECT length, AVG(replacement_cost) AS avg_replacement_cost FROM public.film
GROUP BY length
ORDER BY length DESC 
LIMIT 10



