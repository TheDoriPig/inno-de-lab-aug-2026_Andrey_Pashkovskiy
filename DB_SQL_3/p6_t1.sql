SELECT
	o.order_id,
	o.customer_id,
	o.item,
	o.amount,
	SUM(o.amount) OVER(PARTITION BY o.customer_id ORDER BY o.order_id) AS total_by_customer
FROM orders o 
ORDER BY o.order_id 