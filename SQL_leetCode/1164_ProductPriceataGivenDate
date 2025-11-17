WITH target_prices AS (
    SELECT DISTINCT ON (product_id)
        product_id,
        new_price as price
    FROM products
    WHERE change_date <= '2019-08-16'
    ORDER BY product_id, change_date DESC
)

SELECT 
    p.product_id,
    COALESCE(tp.price, 10) as price
FROM (SELECT DISTINCT product_id FROM products) p
LEFT JOIN target_prices tp USING(product_id);
