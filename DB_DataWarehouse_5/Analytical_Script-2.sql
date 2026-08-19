--Best-selling products in each category
SELECT 
    dp.product_name,
    pc.category_name,
    SUM(foi.quantity) AS units_sold,
    SUM(foi.total_price) AS revenue
FROM fact_order_items foi
JOIN dim_products dp ON foi.product_id = dp.product_id
JOIN product_category pc ON dp.category_id = pc.category_id
GROUP BY dp.product_name, pc.category_name
ORDER BY revenue DESC
LIMIT 10;
