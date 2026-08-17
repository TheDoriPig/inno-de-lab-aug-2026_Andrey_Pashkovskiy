SELECT
	s.status,
	c.first_name,
	c.last_name 
FROM customers c 
INNER JOIN shippings s 
	ON c.customer_id = s.customer