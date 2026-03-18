# Problem: Product Sales Analysis I
# Goal: Master basic `INNER JOIN` in SQL.

/* TODO: Write your SQL query to join Sales and Product tables on product_id */
SELECT p.product_name, s.year, s.price
FROM Sales s
INNER JOIN Product p ON s.product_id=p.product_id;