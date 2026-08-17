SELECT 
	c.first_name,
	c.last_name,
	o.item,
	o.amount
FROM customers c 
LEFT JOIN orders o
	ON c.customer_id = o.customer_id 
WHERE o.order_id IS NOT NULL