/*
You are given a table, Projects, containing three columns: Task_ID, Start_Date and End_Date. 
It is guaranteed that the difference between the End_Date and the Start_Date is equal to 
1 day for each row in the table.

If the End_Date of the tasks are consecutive, then they are part of the same project. 
Samantha is interested in finding the total number of different projects completed.

Write a query to output the start and end dates of projects listed by the number of days 
it took to complete the project in ascending order. If there is more than one project that 
have the same number of completion days, then order by the start date of the project.
*/

WITH Temp AS(
    SELECT 
        Start_Date,
        End_Date,
        ROW_NUMBER() OVER(ORDER BY Start_Date) AS Row_Num
    FROM
        Projects
)

SELECT
    MIN(Start_Date),
    MAX(End_Date)
FROM
    Temp
GROUP BY
    DATEDIFF(day, Row_Num, Start_Date)
ORDER BY
    COUNT(DATEDIFF(day, Row_Num, Start_Date)),
    MIN(Start_Date);

