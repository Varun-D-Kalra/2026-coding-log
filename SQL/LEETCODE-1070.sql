WITH first_yr AS (
    SELECT product_id, MIN(year) AS first
    FROM Sales
    GROUP BY product_id
)
SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales s
JOIN first_yr f
  ON s.product_id = f.product_id
 AND s.year = f.first;


# Done this after a break, or it would feel hard at first attempt. Actually its easy tho.
