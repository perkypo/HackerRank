/*
Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy: 

Given the table schemas below, write a query to print the company_code, founder name, 
total number of lead managers, total number of senior managers, total number of 
managers, and total number of employees. Order your output by ascending company_code.

Note:

The tables may contain duplicate records.
The company_code is string, so the sorting should not be numeric. For example, if 
the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.
*/

SELECT
    C.company_code,
    C.founder,
    COUNT(DISTINCT L.lead_manager_code),
    COUNT(DISTINCT S.senior_manager_code),
    COUNT(DISTINCT M.manager_code),
    COUNT(DISTINCT E.employee_code)
FROM
    Company C,
    Lead_Manager L,
    Senior_Manager S,
    Manager M,
    Employee E
WHERE
    L.company_code =C.company_code and
    S.lead_manager_code = L.lead_manager_code and
    M.senior_manager_code = S.senior_manager_code and
    E.manager_code = M.manager_code
GROUP BY
    C.company_code, C.founder
ORDER BY
    C.company_code;
