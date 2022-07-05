SELECT
    city.city_name,
    product.product_name,
    ROUND(SUM(product.current_price)) as amount_spent
FROM
    city
    INNER JOIN customer ON customer.city_id = city.id
    INNER JOIN invoice ON invoice.customer_id = customer.id
    INNER JOIN invoice_item ON invoice_item.invoice_id = invoice.id
    INNER JOIN product ON product.id = invoice_item.product_id\
GROUP BY
    city.city_name,
    product.product_name
ORDER BY
    amount_spent DESC,
    city.city_name,
    product.product_name