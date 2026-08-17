SELECT 
	c.country,
	count(*)
FROM customers c 
GROUP BY c.country 