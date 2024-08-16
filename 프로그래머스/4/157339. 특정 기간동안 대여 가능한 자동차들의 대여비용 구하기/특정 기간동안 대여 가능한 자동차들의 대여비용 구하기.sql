select CAR_ID,CAR_TYPE,round(DAILY_FEE*30*(1-DISCOUNT_RATE/100)) FEE from CAR_RENTAL_COMPANY_CAR join (select CAR_TYPE,DISCOUNT_RATE from CAR_RENTAL_COMPANY_DISCOUNT_PLAN where 
DURATION_TYPE="30일 이상") A using(car_type)
where CAR_TYPE in ('세단','SUV') and CAR_ID not in 
(select distinct car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where 
 start_date <="20221130" and end_date > "20221101")
and DAILY_FEE*30*(1-DISCOUNT_RATE/100) between 500000 and 2000000
order by fee desc,car_type,car_id desc

