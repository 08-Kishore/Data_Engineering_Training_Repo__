SET SQL_SAFE_UPDATES = 0;
CREATE TABLE food_orders (
    order_id INT PRIMARY KEY,
    restaurant VARCHAR(100),
    city VARCHAR(50),
    food_type VARCHAR(50),
    order_amount DECIMAL(10,2),
    delivery_partner VARCHAR(50),
    order_date DATE
);
INSERT INTO food_orders VALUES
(101, 'Spice Hub', 'Hyderabad', 'Indian', 850, 'Ravi', '2026-09-01'),
(102, 'Burger Zone', 'Hyderabad', 'Fast Food', 520, 'Kiran', '2026-09-01'),
(103, 'Pizza Point', 'Mumbai', 'Fast Food', 1100, 'Ravi', '2026-09-02'),
(104, 'Curry House', 'Bangalore', 'Indian', 760, 'Aman', '2026-09-02'),
(105, 'Spice Hub', 'Hyderabad', 'Indian', 1250, 'Kiran', '2026-09-03'),
(106, 'Sushi World', 'Mumbai', 'Japanese', 1800, 'Aman', '2026-09-03'),
(107, 'Pizza Point', 'Mumbai', 'Fast Food', 900, 'Ravi', '2026-09-04'),
(108, 'Curry House', 'Bangalore', 'Indian', 640, 'Kiran', '2026-09-04'),
(109, 'Burger Zone', 'Hyderabad', 'Fast Food', 430, 'Aman', '2026-09-05'),
(110, 'Sushi World', 'Mumbai', 'Japanese', 2100, 'Ravi', '2026-09-05'),
(111, 'Spice Hub', 'Hyderabad', 'Indian', 950, 'Aman', '2026-09-06'),
(112, 'Curry House', 'Bangalore', 'Indian', 880, 'Ravi', '2026-09-06');

select count(*) from food_orders;
select sum(order_amount) from food_orders;
select avg(order_amount) from food_orders;
select * from food_orders order by order_amount desc limit 1;
select * from food_orders order by order_amount asc limit 1;

select city,sum(order_amount) from food_orders group by city order by city;
select food_type,avg(order_amount) from food_orders group by food_type;
select delivery_partner,sum(order_amount) from food_orders group by delivery_partner; 
SELECT 
    restaurant,
    SUM(order_amount) AS total_amount
FROM food_orders
GROUP BY restaurant
HAVING SUM(order_amount) > 2000;

SELECT 
    delivery_partner,
    SUM(order_amount) AS total_amount
FROM food_orders
GROUP BY delivery_partner
HAVING avg(order_amount) > 800;

SELECT 
    food_type,
    SUM(order_amount) AS total_amount
FROM food_orders
GROUP BY food_type
HAVING SUM(order_amount) > 2500;

select city,sum(order_amount) as 'total_revenue'
from food_orders
group by city
order by total_revenue desc;

select restaurant,sum(order_amount) as 'total_revenue'
from food_orders
group by restaurant
order by total_revenue desc limit 1;