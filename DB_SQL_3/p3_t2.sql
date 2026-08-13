SELECT 
	o.item,
	count(*),
	AVG(o.amount)
FROM orders o 
GROUP BY o.item 