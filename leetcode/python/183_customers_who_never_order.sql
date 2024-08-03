-- https://leetcode.com/problems/customers-who-never-order/

SELECT c.name as Customers
FROM Customers as c
LEFT JOIN Orders as o on c.id = o.customerID
WHERE o.id IS NULL
