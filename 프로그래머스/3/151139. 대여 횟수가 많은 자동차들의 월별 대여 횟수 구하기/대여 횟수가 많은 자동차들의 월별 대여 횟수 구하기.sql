select month(start_date) MONTH,car_id CAR_ID,count(*) RECORDS from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where date_format(start_date,'%y%m') in("2208","2209","2210") and car_id in (
    select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY  
    where date_format(start_date,'%y%m') in("2208","2209","2210") 
    group by car_id having count(*) >= 5
)
group by month(start_date),car_id
order by 1,2 desc
