--Write a solution to find employees who have the highest salary in each of the departments.
--
--Return the result table in any order.
--
--The result format is in the following example.

SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM (
    SELECT
        *,
        DENSE_RANK() OVER (
            PARTITION BY departmentId
            ORDER BY salary DESC
        ) AS rk
    FROM Employee
) e
JOIN Department d ON e.departmentId = d.id
WHERE rk = 1;


--or can be another solution withщге     windows

SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE e.salary = (
    SELECT MAX(salary)
    FROM Employee
    WHERE departmentId = e.departmentId
);
