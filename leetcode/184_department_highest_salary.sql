

SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM 
    Employee as e
    JOIN (
        SELECT departmentId, MAX(salary) as salary
        FROM Employee
        GROUP BY departmentId
    ) as m on e.departmentId = m.departmentId and e.salary = m.salary
    JOIN Department as d on e.departmentId = d.id
    
