-- 코드를 입력하세요
-- REGEXP 'cond1|cond2': column에 cond1, cond2가 포함된 경우 전부 return
SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE REGEXP 'Neutered|Spayed', 'O', 'X') AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID