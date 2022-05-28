-- https://leetcode.com/problems/delete-duplicate-emails/submissions/
-- DELETE는 SELECT이랑 쓸 수 없음

DELETE FROM person
WHERE id NOT IN(
    SELECT m.min_id
    FROM(
        SELECT MIN(p.id) as min_id
        FROM Person as p
        GROUP BY p.email
    ) as m
)