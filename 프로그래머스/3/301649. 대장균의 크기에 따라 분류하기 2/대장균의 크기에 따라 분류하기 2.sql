select ID,
case 
when rank() over(order by SIZE_OF_COLONY desc)/(select count(*) from ecoli_data)<=0.25 then "CRITICAL"
when rank() over(order by SIZE_OF_COLONY desc)/(select count(*) from ecoli_data)<=0.50 then "HIGH"
when rank() over(order by SIZE_OF_COLONY desc)/(select count(*) from ecoli_data)<=0.75 then "MEDIUM"
else "LOW"
end
COLONY_NAME 
from ECOLI_DATA 
order by id