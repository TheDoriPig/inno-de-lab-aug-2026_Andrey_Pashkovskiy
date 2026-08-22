--We can view the top customers of our store (honestly, I don't think this is practical for a large store, but the capability exists).
SELECT 
    du.first_name,
    du.last_name,
    du.user_id,
    SUM(foi.total_price)
FROM fact_order_items foi
JOIN dim_user du 
	ON foi.user_id = du.user_id
GROUP BY du.user_id 
ORDER BY SUM(foi.total_price) DESC
LIMIT 10;
