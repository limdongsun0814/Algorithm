select count(*) fish_count ,month(time) month from fish_info 
group by month
order by month