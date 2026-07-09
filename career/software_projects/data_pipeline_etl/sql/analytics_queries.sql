-- Analytics queries for the e-commerce SQLite warehouse (warehouse/ecommerce.db)
-- Run with:  sqlite3 warehouse/ecommerce.db < sql/analytics_queries.sql
-- Each query is standalone; comment/uncomment as needed.

-- 1. Top 5 products by total revenue -------------------------------------- --
SELECT p.product_id,
       p.name,
       p.category,
       SUM(f.quantity)               AS units_sold,
       ROUND(SUM(f.revenue), 2)      AS total_revenue
FROM   fact_sales f
JOIN   dim_product p ON p.product_id = f.product_id
GROUP  BY p.product_id, p.name, p.category
ORDER  BY total_revenue DESC
LIMIT  5;

-- 2. Daily revenue trend --------------------------------------------------- --
SELECT order_date,
       COUNT(*)                      AS orders,
       ROUND(SUM(revenue), 2)        AS daily_revenue
FROM   fact_sales
GROUP  BY order_date
ORDER  BY order_date;

-- 3. Revenue by product category ------------------------------------------ --
SELECT p.category,
       COUNT(*)                      AS orders,
       ROUND(SUM(f.revenue), 2)      AS category_revenue
FROM   fact_sales f
JOIN   dim_product p ON p.product_id = f.product_id
GROUP  BY p.category
ORDER  BY category_revenue DESC;

-- 4. Top customers by spend ------------------------------------------------ --
SELECT c.customer_id,
       c.name,
       c.city,
       COUNT(*)                      AS orders,
       ROUND(SUM(f.revenue), 2)      AS lifetime_value
FROM   fact_sales f
JOIN   dim_customer c ON c.customer_id = f.customer_id
GROUP  BY c.customer_id, c.name, c.city
ORDER  BY lifetime_value DESC
LIMIT  5;

-- 5. Overall KPIs ---------------------------------------------------------- --
SELECT COUNT(*)                            AS total_orders,
       COUNT(DISTINCT customer_id)         AS active_customers,
       ROUND(SUM(revenue), 2)              AS gross_revenue,
       ROUND(AVG(revenue), 2)              AS avg_order_value
FROM   fact_sales;
