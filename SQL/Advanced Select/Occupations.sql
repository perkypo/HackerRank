/*
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its 
corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

Note: Print NULL when there are no more names corresponding to an occupation.
*/

SELECT [Doctor], [Professor], [Singer], [Actor]
FROM
(
    SELECT ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) [RowNum], * FROM OCCUPATIONS
) AS temp
PIVOT
(
    MAX(Name) FOR Occupation IN ([Doctor], [Professor], [Singer], [Actor])
) AS P