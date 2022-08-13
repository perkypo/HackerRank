/*
You are given two tables: Students and Grades. Students contains three columns ID, Name and Marks.

Grades contains the following data:
        WHEN Marks >=90 THEN 10
        WHEN Marks >=80 THEN 9
        WHEN Marks >=70 THEN 8
        WHEN Marks >=60 THEN 7
        WHEN Marks >=50 THEN 6
        WHEN Marks >=40 THEN 5
        WHEN Marks >=30 THEN 4
        WHEN Marks >=20 THEN 3
        WHEN Marks >=10 THEN 2
        WHEN Marks >=0  THEN 1

Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. 
Ketty doesn't want the NAMES of those students who received a grade lower than 8. 
The report must be in descending order by grade -- i.e. higher grades are entered first. 
If there is more than one student with the same grade (8-10) assigned to them, order those 
particular students by their name alphabetically. Finally, if the grade is lower than 8, 
use "NULL" as their name and list them by their grades in descending order. If there is more 
than one student with the same grade (1-7) assigned to them, order those particular students 
by their marks in ascending order.

Write a query to help Eve.
*/


SELECT
    CASE
        WHEN Marks >=70 THEN Name
        ELSE 'NULL'
    END as Name,
    CASE
        WHEN Marks >=90 THEN 10
        WHEN Marks >=80 THEN 9
        WHEN Marks >=70 THEN 8
        WHEN Marks >=60 THEN 7
        WHEN Marks >=50 THEN 6
        WHEN Marks >=40 THEN 5
        WHEN Marks >=30 THEN 4
        WHEN Marks >=20 THEN 3
        WHEN Marks >=10 THEN 2
        ELSE 1
    END as Grade,
    Marks
FROM
    Students
ORDER BY
    Grade DESC,
    Name,
    Marks;