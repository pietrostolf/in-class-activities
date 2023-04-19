SELECT * FROM address
ORDER BY address_id ASC

SELECT * FROM city
ORDER BY city_id ASC 

SELECT city_id, city FROM city
WHERE city IN ('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes')
ORDER BY city_id ASC 


SELECT city.city_id, city.city, address.district FROM city
JOIN address
ON city.city_id = address.city_id
WHERE city IN ('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes')
ORDER BY city_id ASC 

SELECT district
	FROM public.address
	WHERE city_id in (	
					SELECT city_id
					FROM public.city
					WHERE city in ('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes')
		)