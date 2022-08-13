/*You are given three tables: Students, Friends and Packages. Students contains 
two columns: ID and Name. Friends contains two columns: ID and Friend_ID (ID of 
the ONLY best friend). Packages contains two columns: ID and Salary (offered salary in $ thousands per month).



Write a query to output the names of those students whose best friends got 
offered a higher salary than them. Names must be ordered by the salary amount 
offered to the best friends. It is guaranteed that no two students got same salary offer.

*/

SELECT
    S.Name
FROM
    STUDENTS S 
    INNER JOIN Packages P ON S.ID = P.ID
    INNER JOIN Friends F ON F.ID = S.ID
    INNER JOIN Packages P1 ON F.Friend_ID = P1.ID
WHERE
    P.Salary < P1.Salary
ORDER BY
    P1.Salary;