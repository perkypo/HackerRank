/* P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

* 
* * 
* * * 
* * * * 
* * * * *
Write a query to print the pattern P(20).*/


DECLARE @count INT = 1;
WHILE (@count <= 20)
BEGIN
    PRINT replicate('* ', @count)
    SET @count = @count + 1
END;