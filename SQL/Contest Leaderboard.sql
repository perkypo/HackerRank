/* You did such a great job helping Julia with her last coding contest 
challenge that she wants you to work on this one, too!

The total score of a hacker is the sum of their maximum scores for all of 
the challenges. Write a query to print the hacker_id, name, and total 
score of the hackers ordered by the descending score. If more than one 
hacker achieved the same total score, then sort the result by ascending 
hacker_id. Exclude all hackers with a total score of 0 from your result.
*/

SELECT
    H.hacker_id,
    H.name,
    SUM(temp.score) AS total_score
FROM
    Hackers H INNER JOIN
    (SELECT 
        hacker_id, 
        challenge_id, 
        max(score) AS score
    FROM
        Submissions
     GROUP BY
        hacker_id,
        challenge_id
    )temp ON temp.hacker_id = H.hacker_id
GROUP BY
    H.hacker_id,
    H.name
HAVING
    SUM(temp.score)>0
ORDER BY
    SUM(temp.score) DESC,
    H.hacker_id;