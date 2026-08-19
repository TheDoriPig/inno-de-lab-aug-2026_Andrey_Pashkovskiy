--To see which category is the most profitable (or if sorting by total_units_sold the best-selling)
SELECT 
    pc.category_name,
    SUM(foi.quantity) AS total_units_sold,
    SUM(foi.total_price) AS total_revenue
FROM fact_order_items foi
JOIN dim_products dp ON foi.product_id = dp.product_id
JOIN product_category pc ON dp.category_id = pc.category_id
GROUP BY pc.category_name
ORDER BY total_revenue DESC;