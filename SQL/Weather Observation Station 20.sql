/*A median is defined as a number separating the higher half of a data 
set from the lower half. Query the median of the Northern Latitudes 
(LAT_N) from STATION and round your answer to 4 decimal places.
*/

SELECT
    CASE
        WHEN COUNT(LAT_N)%2<>0 THEN 
FROM
    (SELECT LAT_N FROM STATION ORDER BY LAT_N)
;