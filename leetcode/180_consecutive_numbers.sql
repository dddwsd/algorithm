-- LEAD 다음 row - MSSQL
SELECT DISTINCT c.num as ConsecutiveNums
FROM (
    SELECT 
        num,
        LEAD(num, 1) OVER (ORDER BY id) as next,
        LEAD(num, 2) OVER (ORDER BY id) as next_next
    FROM
        Logs
) as c
WHERE c.num = c.next and c.num = c.next_next


-- LAG 이전 row - MSSQL
SELECT DISTINCT c.num as ConsecutiveNums
FROM (
    SELECT 
        num,
        LAG(num, 1) OVER (ORDER BY id) as before,
        LAG(num, 2) OVER (ORDER BY id) as before_before
    FROM
        Logs
) as c
WHERE c.num = c.before and c.num = c.before_before

-- LEFT JOIN - MySQL
SELECT DISTINCT l.num as ConsecutiveNums
FROM
    Logs as l
    LEFT JOIN Logs as l_next on l.id + 1 = l_next.id
    LEFT JOIN Logs as l_next_next on l.id + 2 = l_next_next.id
WHERE l.num = l_next.num AND l.num = l_next_next.num
