select PRODUCT_ID,PRODUCT_NAME,TOTAL_COUNT*PRICE TOTAL_SALES 
from FOOD_PRODUCT join 
(select PRODUCT_ID, sum(amount) TOTAL_COUNT from food_order
where date_format(PRODUCE_DATE,"%y%m")="2205"
group by product_id) A using(PRODUCT_ID)
order by total_sales desc,PRODUCT_ID
