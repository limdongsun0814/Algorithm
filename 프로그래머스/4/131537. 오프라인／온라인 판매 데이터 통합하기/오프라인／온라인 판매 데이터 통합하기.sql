select date_format(SALES_DATE,'%Y-%m-%d') SALES_DATE,PRODUCT_ID,USER_ID,SALES_AMOUNT 
from ONLINE_SALE 
where SALES_DATE like ("2022-03%")
union
select date_format(SALES_DATE,'%Y-%m-%d') SALES_DATE,PRODUCT_ID,null USER_ID,SALES_AMOUNT
from offline_sale
where SALES_DATE like ("2022-03%")
order by SALES_DATE,PRODUCT_ID,user_id