--Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
--
--The result format is in the following example.

-- Write your PostgreSQL query statement below
SELECT (SELECT DISTINCT salary FROM Employee
ORDER BY salary DESC OFFSET 1 LIMIT 1) as SecondHighestSalary