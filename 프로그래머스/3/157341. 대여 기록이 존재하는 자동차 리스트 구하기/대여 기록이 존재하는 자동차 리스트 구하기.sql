select car_id from CAR_RENTAL_COMPANY_CAR join 
(select distinct car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where date_format(START_DATE,'%m')='10') car using(car_id) where car_type='세단' order by 1 desc