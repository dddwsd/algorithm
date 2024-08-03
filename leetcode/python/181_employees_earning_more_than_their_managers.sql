-- https://leetcode.com/problems/employees-earning-more-than-their-managers/

SELECT el.name as Employee
FROM Employee as el
JOIN Employee as er on el.managerID = er.id and el.salary > er.salary
