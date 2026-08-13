SELECT
	o.order_id,
	o.item,
	o.amount,
	o.customer_id 
FROM orders o
WHERE amount > 1000