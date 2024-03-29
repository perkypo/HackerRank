/* Consider P1(a,c) and P2(b,d) to be two points on a 2D plane where (a,b) 
are the respective minimum and maximum values of Northern Latitude (LAT_N) 
and (c,d) are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.
*/

SELECT
    ROUND(POWER(POWER(MIN(LAT_N)-MAX(LAT_N),2) + POWER(MIN(LONG_W)-MAX(LONG_W),2),0.5),4)
FROM
    STATION;
    