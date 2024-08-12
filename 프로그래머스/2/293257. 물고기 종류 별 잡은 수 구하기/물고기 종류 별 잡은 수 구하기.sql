select count(*) fish_count,fish_name 
from FISH_INFO join FISH_NAME_INFO using(fish_type)
group by fish_name
order by fish_count desc