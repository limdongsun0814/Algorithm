select animal_outs.ANIMAL_ID,animal_outs.NAME from animal_ins right join animal_outs using(animal_id)
where isNull(animal_ins.ANIMAL_ID)
order by 1,2