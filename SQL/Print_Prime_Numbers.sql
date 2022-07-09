/*
Write a query to print all prime numbers less than or equal to 1000. 
Print your result on a single line, and use the ampersand (&) character 
as your separator (instead of a space).
*/

DECLARE @i SMALLINT 
DECLARE @num SMALLINT  = 5;
DECLARE @flag BIT
DECLARE @Result NVARCHAR(4000)

DECLARE @PrimeNumbers Table(Number INT)

INSERT INTO @PrimeNumbers VALUES (2),(3)

WHILE (@num <= 1000)
BEGIN
    SET @i = 2
    SET @flag = 1
    WHILE(@i <= SQRT(@num))
    BEGIN
        IF(@num%@i = 0)
            SET @flag = 0
        SET @i += 1
    END
    IF(@flag = 1)
        INSERT INTO @PrimeNumbers VALUES (@num)
    SET @num += 2
END

SELECT  @Result = COALESCE(@Result + '&','') + CAST(Number AS VARCHAR(10))
FROM @PrimeNumbers WHERE Number IS NOT NULL

SELECT @Result