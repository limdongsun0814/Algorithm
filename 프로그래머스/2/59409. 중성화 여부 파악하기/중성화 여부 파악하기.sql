select ANIMAL_ID,name,
case 
when SEX_UPON_INTAKE like ("%Neutered%") or 
SEX_UPON_INTAKE like ("%Spayed%") then "O"
else "X"
end 중성화
from animal_ins
order by animal_id