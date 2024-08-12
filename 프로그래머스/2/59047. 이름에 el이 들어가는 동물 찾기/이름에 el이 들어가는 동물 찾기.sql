select ANIMAL_ID,name 
from ANIMAL_INS 
where upper(name) like ("%EL%") and animal_type = "Dog"
order by upper(name)