-- 코드를 입력하세요
SELECT ANIMAL_ID, ANIMAL_INS.ANIMAL_TYPE, ANIMAL_INS.NAME 
from ANIMAL_INS join ANIMAL_OUTS using(animal_id)
where SEX_UPON_INTAKE like ("%Intact%") and SEX_UPON_OUTCOME not like ("%Intact%")
order by 1