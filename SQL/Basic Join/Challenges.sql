/*
Julia asked her students to create some coding challenges. Write a query to print the hacker_id, name, 
and the total number of challenges created by each student. Sort your results by the total number of 
challenges in descending order. If more than one student created the same number of challenges, 
then sort the result by hacker_id. If more than one student created the same number of challenges and 
the count is less than the maximum number of challenges created, then exclude those students from the result.
*/

WITH temp
AS
(
    SELECT
        h.hacker_id AS hacker_id,
        h.name AS name,
        COUNT(c.challenge_id) as challenge_count
    FROM
        Hackers h INNER JOIN
        Challenges c ON c.hacker_id = h.hacker_id
    GROUP BY
        h.hacker_id, h.name
)

SELECT
    hacker_id,
    name,
    challenge_count
FROM
    temp
WHERE
    challenge_count = (SELECT 
                            MAX(challenge_count) 
                       FROM 
                            temp)
    OR
    challenge_count IN (SELECT 
                            challenge_count 
                        FROM 
                            temp 
                        GROUP BY 
                            challenge_count 
                        HAVING 
                            count(challenge_count) = 1)
ORDER BY
    challenge_count DESC,
    hacker_id;