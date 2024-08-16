select HISTORY_ID,round(
case
when datediff(END_DATE,start_date)+1 >= 90 
then (datediff(END_DATE,start_date)+1 )*DAILY_FEE*(100-
 (select discount_rate from CAR_RENTAL_COMPANY_DISCOUNT_PLAN  where CAR_TYPE="트럭" and DURATION_TYPE="90일 이상"))/100
 when datediff(END_DATE,start_date)+1 >= 30 
then (datediff(END_DATE,start_date)+1 )*DAILY_FEE*(100-
 (select discount_rate from CAR_RENTAL_COMPANY_DISCOUNT_PLAN  where CAR_TYPE="트럭" and DURATION_TYPE="30일 이상"))/100
  when datediff(END_DATE,start_date)+1 >= 7 
then (datediff(END_DATE,start_date)+1 )*DAILY_FEE*(100-
 (select discount_rate from CAR_RENTAL_COMPANY_DISCOUNT_PLAN  where CAR_TYPE="트럭" and DURATION_TYPE="7일 이상"))/100
 else  (datediff(END_DATE,start_date)+1 )*DAILY_FEE
end) fee
from CAR_RENTAL_COMPANY_RENTAL_HISTORY join CAR_RENTAL_COMPANY_CAR using(CAR_ID)
where 
CAR_ID in (select car_id from CAR_RENTAL_COMPANY_CAR  where car_Type="트럭")
order by fee desc,history_id desc