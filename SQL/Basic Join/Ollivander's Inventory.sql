/*
Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.

Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to 
buy each non-evil wand of high power and age. Write a query to print the id, age, coins_needed, and 
power of the wands that Ron's interested in, sorted in order of descending power. If more than one wand 
has same power, sort the result in order of descending age.


SELECT
    wp.age,
    MIN(w.coins_needed),
    w.power
FROM
    Wands w INNER JOIN
    Wands_Property wp ON wp.code=w.code
GROUP BY
    wp.age,
    w.power
ORDER BY
    w.power DESC,
    wp.age DESC;

*/


SELECT
    w.id,
    wp.age,
    w.coins_needed,
    w.power
FROM
    Wands w INNER JOIN
    Wands_Property wp ON wp.code=w.code
WHERE
    wp.is_evil=0 AND 
    w.coins_needed = (
        SELECT
            MIN(w1.coins_needed)
        FROM
            Wands w1 INNER JOIN
            Wands_Property wp1 ON wp1.code=w1.code
        WHERE
            w1.power = w.power AND
            wp1.age = wp.age)
ORDER BY
    w.power DESC,
    wp.age DESC;