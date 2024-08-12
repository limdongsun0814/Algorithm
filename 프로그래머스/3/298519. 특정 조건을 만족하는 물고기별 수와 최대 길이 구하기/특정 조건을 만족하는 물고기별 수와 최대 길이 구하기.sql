select count(*) FISH_COUNT,max(length) MAX_LENGTH,FISH_TYPE 
from fish_info
group by FISH_TYPE
having avg(ifnull(length,10))>=33
order by fish_type