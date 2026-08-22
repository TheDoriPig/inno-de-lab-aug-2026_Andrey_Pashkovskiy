--We can see on which days the store generated the highest profit (for example, during holidays or sales)
SELECT 
    dd.full_date AS Date,
    SUM(foi.total_price)
FROM fact_order_items foi
JOIN dim_date dd 
	ON foi.date_id = dd.date_id
GROUP BY dd.full_date
ORDER BY SUM(foi.total_price) DESC;


--Or the highest sales volume
SELECT 
    dd.full_date AS Date,
    SUM(foi.quantity)
FROM fact_order_items foi
JOIN dim_date dd 
	ON foi.date_id = dd.date_id
GROUP BY dd.full_date
ORDER BY SUM(foi.quantity) DESC;
