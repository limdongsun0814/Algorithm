select car_id,round(avg(datediff(END_DATE,START_DATE)+1),1) AVERAGE_DURATION from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
group by CAR_ID
having AVERAGE_DURATION>7
order by AVERAGE_DURATION desc, car_id desc

