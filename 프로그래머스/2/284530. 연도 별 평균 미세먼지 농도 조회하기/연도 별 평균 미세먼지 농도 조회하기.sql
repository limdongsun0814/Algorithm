select YEAR(YM) YEAR
, round(avg(PM_VAL1),2) "PM10"
, round(avg(PM_VAL2),2) "PM2.5" 
from AIR_POLLUTION 
where LOCATION2="수원"
group by YEAR
order by year