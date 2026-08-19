--I use my table from homework 2 and a little upgrade them
--These symbols ?? mean that I am not sure about the correctness of what i written
--Create snowflake dimention(??Which??)
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
CREATE TABLE dim_date (
    date_id INT PRIMARY KEY,
    full_date DATE NOT NULL
);

--Create orders ??dimensions?? (When? and Who?)
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    date_key INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES dim_user(user_id),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_id)
);

--Create fact table(How much?)
CREATE TABLE fact_order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL,
    total_price DECIMAL(10, 2) GENERATED ALWAYS AS (quantity * unit_price) STORED, --Added a calculation of the total cost
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES dim_products(product_id)
);