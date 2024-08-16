select animal_ins.NAME,animal_ins.datetime datetime from animal_ins left join animal_outs using(animal_id)
where isNull(animal_outs.animal_id) 
order by animal_ins.datetime limit 3