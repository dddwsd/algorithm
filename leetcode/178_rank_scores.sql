-- 8.0부터 rank 함수 지원
-- 동일값에 대한 순위를 매길 수 있음.

-- DENSE_RANK - 다음 순위는 중복 순위와 상관없이 순차적으로
-- RANK - 다음 순위는 해당 개수만큼 건너뛰고 진행.

SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) as 'rank'
FROM Scores