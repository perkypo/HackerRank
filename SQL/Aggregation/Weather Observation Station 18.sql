/* Consider P1(a,b) and P2(c,d) to be two points on a 2D plane.

 happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
 happens to equal the minimum value in Western Longitude (LONG_W in STATION).
 happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
 happens to equal the maximum value in Western Longitude (LONG_W in STATION).
Query the Manhattan Distance between points P1 and P2 and round it to a scale of  decimal places.

SELECT CAST(
(
    (SELECT
        MAX(lower_half)
    FROM
        (SELECT
            TOP 50 PERCENT LAT_N AS lower_half
        FROM
            STATION
        ORDER BY
            LAT_N
        ) AS lower_median
    )
    +
    (SELECT
        MIN(higher_half)
    FROM
        (SELECT
            TOP 50 PERCENT LAT_N AS higher_half
        FROM
            STATION
        ORDER BY
            LAT_N DESC
        ) AS higher_median
    ) 
) /2 AS DECIMAL(10,4))

*/

SELECT DISTINCT
    CAST(
        PERCENTILE_DISC(0.5) 
        WITHIN GROUP(ORDER BY LAT_N) 
        OVER()
        AS DECIMAL(10,4)
    )
FROM
    STATION