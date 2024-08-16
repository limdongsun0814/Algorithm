-- 코드를 입력하세요
SELECT FLAVOR
from (
select FLAVOR,TOTAL_ORDER from FIRST_HALF 
union
select FLAVOR,TOTAL_ORDER from JULY 
) total
group by FLAVOR
order by sum(TOTAL_ORDER) desc limit 3
