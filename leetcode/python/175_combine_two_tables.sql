-- https://leetcode.com/problems/combine-two-tables/

SELECT p.firstName, p.lastName, a.city, a.state
FROM Person as p
LEFT JOIN Address as a on p.personId = a.personId
