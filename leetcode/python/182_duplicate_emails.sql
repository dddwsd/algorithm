-- https://leetcode.com/problems/duplicate-emails/

SELECT e.email
FROM (
    SELECT email, count(email) as count
    FROM Person
    GROUP BY email
) as e
WHERE e.count > 1

-- having 절은 GROUP BY절의 기준 항목이나 소그룹의 집계 함수를 이용한 조건을 표시할 수 있다.
SELECT email
FROM Person
GROUP BY email
HAVING count(*) > 1