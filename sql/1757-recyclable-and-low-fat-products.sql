# Problem: Recyclable and Low Fat Products
# Goal: Master multiple AND conditions in SQL.

/* TODO: Find the ids of products that are both low fat and recyclable. */
SELECT product_id
FROM Products
WHERE low_fats="Y" AND recyclable="Y";