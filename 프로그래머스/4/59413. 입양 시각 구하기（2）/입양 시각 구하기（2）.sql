with recursive number as (
    select 0 as HOUR
    union all
    select HOUR+1 from number
    where HOUR<23
)

select HOUR,ifnull(count,0) count from number left join 
(select hour(DATETIME) HOUR,count(ANIMAL_ID) count from ANIMAL_OUTS 
group by hour(DATETIME)) A using(HOUR)
order by HOUR