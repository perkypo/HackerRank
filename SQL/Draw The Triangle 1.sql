/* P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

* * * * * 
* * * * 
* * * 
* * 
*
Write a query to print the pattern P(20).

*/

DECLARE @count INT = 20;
WHILE (@count > 0)
BEGIN
    PRINT replicate('* ', @count)
    SET @count = @count - 1
END;