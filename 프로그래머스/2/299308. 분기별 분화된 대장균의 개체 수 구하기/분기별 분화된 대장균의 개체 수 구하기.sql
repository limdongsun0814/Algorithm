select 
case 
when date_format(DIFFERENTIATION_DATE,"%m") in("01","02","03") then "1Q"
when date_format(DIFFERENTIATION_DATE,"%m") in("04","05","06") then "2Q"
when date_format(DIFFERENTIATION_DATE,"%m") in("07","08","09") then "3Q"
when date_format(DIFFERENTIATION_DATE,"%m") in("10","11","12") then "4Q"
end QUARTER,
count(*) ECOLI_COUNT
from ECOLI_DATA 
group by QUARTER
order by QUARTER