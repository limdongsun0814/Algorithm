select Year(sales_date) year, month(sales_date) month,gender,count(distinct user_id) users
from user_info join online_sale using(user_id)
where gender is not null 
group by year,month,gender
order by 1,2,3