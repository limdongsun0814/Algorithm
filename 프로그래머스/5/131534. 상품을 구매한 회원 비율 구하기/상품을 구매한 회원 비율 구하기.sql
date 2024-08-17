select year(SALES_DATE) year,month(SALES_DATE) month,count(distinct user_id) PURCHASED_USERS,
round(count(distinct user_id)/(select count(*) from user_info where date_format(joined,'%Y') = "2021"),1) PUCHASED_RATIO
from ONLINE_SALE left join USER_INFO using(user_id)
where date_format(joined,'%Y') = "2021"
group by year, month
order by year,month