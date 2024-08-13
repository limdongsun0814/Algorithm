select car_id,if(대여중="대여중","대여중","대여 가능") AVAILABILITY from 
(select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY group by car_id) B
left join
(select car_id,"대여중" from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where "2022-10-16" between start_date and end_date
group by car_id order by 1 desc) A using(car_id)
order by car_id desc