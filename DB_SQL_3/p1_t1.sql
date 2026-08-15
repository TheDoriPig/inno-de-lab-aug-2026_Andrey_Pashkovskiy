SELECT
	c.first_name,
	c.last_name,
	c.age,
	c.country 
FROM customers c
WHERE c.country = 'USA' and c.age > 25