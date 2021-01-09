-- 코드를 입력하세요
SELECT AI.ANIMAL_ID, AI.NAME
FROM ANIMAL_INS AS AI
LEFT JOIN ANIMAL_OUTS AS AO
ON (AI.ANIMAL_ID = AO.ANIMAL_ID)
WHERE AO.DATETIME < AI.DATETIME
ORDER BY AI.DATETIME