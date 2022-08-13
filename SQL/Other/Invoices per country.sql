SELECT
    country.country_name,
    count(invoice.id),
    ROUND(AVG(invoice.total_price),6) as country_avg
FROM
    country 
    INNER JOIN city ON city.country_id  = country.id 
    INNER JOIN customer ON customer.city_id = city.id
    INNER JOIN invoice ON invoice.customer_id = customer.id
GROUP BY
    country.country_name
HAVING
    country_avg>(SELECT AVG(i.total_price) FROM invoice i);