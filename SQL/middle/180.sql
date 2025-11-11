--Find all numbers that appear at least three times consecutively.
--
--Return the result table in any order.
--
--The result format is in the following example.

SELECT DISTINCT num as ConsecutiveNums
FROM (
    SELECT
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev1,
        LAG(num, 2) OVER (ORDER BY id) AS prev2
    FROM Logs
) t
WHERE num = prev1 AND num = prev2;
