SELECT ANIMAL_ID, ANIMAL_INS.name name
from ANIMAL_INS join ANIMAL_OUTS using(animal_id)
order by datediff(ANIMAL_OUTS.DATETIME,ANIMAL_INS.DATETIME)+1 desc limit 2