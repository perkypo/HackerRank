/*
You are given a table, Functions, containing two columns: X and Y.

Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if 
X1 = Y2 and X2 = Y1. 
Write a query to output all such symmetric pairs in ascending order 
by the value of X. List the rows such that X1 ≤ Y1
*/


SELECT
    F1.X,
    F1.Y
FROM
    FUNCTIONS F1 INNER JOIN
    FUNCTIONS F2 ON F1.X = F2.Y AND F2.X = F1.Y
GROUP BY
    F1.X,
    F1.Y
HAVING
    COUNT(F1.X)>1 or F1.X < F1.Y
ORDER BY
    F1.X