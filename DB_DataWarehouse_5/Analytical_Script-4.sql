--We can view the top customers of our store (honestly, I don't think this is practical for a large store, but the capability exists).
SELECT 
    du.first_name,
    du.last_name,
    SUM(foi.total_price)
FROM fact_order_items foi
JOIN orders o ON foi.order_id = o.order_id
JOIN dim_user du ON o.user_id = du.user_id
GROUP BY du.first_name, du.last_name
ORDER BY SUM(foi.total_price) DESC
LIMIT 10;
