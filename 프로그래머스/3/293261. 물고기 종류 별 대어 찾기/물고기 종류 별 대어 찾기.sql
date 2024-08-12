select ID, FISH_NAME, length
from FISH_INFO join FISH_NAME_INFO using(fish_type) 
where (fish_type,length) in 
(select fish_type, max(length) len from FISH_INFO group by fish_type)
