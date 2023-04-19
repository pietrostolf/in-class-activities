SELECT * FROM public.film
ORDER BY film_id ASC 

SELECT avg(rental_rate) FROM public.film 


SELECT rating, AVG(rental_rate) AS avg_rental_cost
FROM film
GROUP BY rating
ORDER BY avg_rental_cost ASC;

SELECT SUM(replacement_cost) AS total_replacement_cost
FROM film

SELECT rating, SUM(replacement_cost) AS total_replacement_cost
FROM film
GROUP BY rating

SELECT MAX(length) AS max_lentgh
FROM film

SELECT * FROM public.film
ORDER BY length DESC 