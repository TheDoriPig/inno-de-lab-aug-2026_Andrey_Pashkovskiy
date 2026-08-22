--I use my table from homework 2 and a little upgrade them
--Create snowflake dimention(What?)
CREATE TABLE product_category (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL UNIQUE 
);

--Create products dimension(What?)
CREATE TABLE dim_products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    category_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES product_category(category_id)
);

--Create user dimension(Who?)
CREATE TABLE dim_user (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

--Create date dimension(When?)
--Add column year, quarter, month, day_of_week, month_name, and day_name for analytics
CREATE TABLE dim_date (
    date_id INT PRIMARY KEY,
    full_date DATE NOT NULL UNIQUE, 
    --Add UNIQUE constraint on full_date to prevent duplicate date entries
    --One date_id can be reused across many fact records
    year INT NOT NULL,
    quarter INT NOT NULL CHECK (quarter BETWEEN 1 AND 4),
    month INT NOT NULL CHECK (month  BETWEEN 1 AND 12),
    day_of_week INT NOT NULL CHECK (day_of_week BETWEEN 1 AND 7),
    month_name VARCHAR(20),
    day_name VARCHAR(20)
);

--Drop order table and add foreign key date_id, user_id in fact_order_items table 
--Create fact table - business action (puschase, transaction)
CREATE TABLE fact_order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    date_id INT NOT NULL,
    user_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL,
    total_price DECIMAL(10, 2) GENERATED ALWAYS AS (quantity * unit_price) STORED, --Added a calculation of the total cost
    FOREIGN KEY (product_id) REFERENCES dim_products(product_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY (user_id) REFERENCES dim_user(user_id)
);
