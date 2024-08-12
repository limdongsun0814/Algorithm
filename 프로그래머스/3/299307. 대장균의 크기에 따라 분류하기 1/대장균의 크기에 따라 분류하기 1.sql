select id,
case
when SIZE_OF_COLONY>1000 then "HIGH"
when SIZE_OF_COLONY>100 then "MEDIUM"
else "LOW"
end 
size
from ecoli_data