-- https://leetcode.com/problems/second-highest-salary/submissions/

SELECT MAX(salary) as SEcondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary)
                FROM Employee)

-- Using LIMIT, OFFSET
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary

-- IFNULL and LIMIT, OFFSET
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
