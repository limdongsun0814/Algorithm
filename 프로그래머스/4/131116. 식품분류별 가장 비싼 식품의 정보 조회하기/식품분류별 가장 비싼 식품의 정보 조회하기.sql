select CATEGORY,price max_price, PRODUCT_NAME from FOOD_PRODUCT 
where (category,price) in (
    select CATEGORY,max(price) price from FOOD_PRODUCT 
    where category in ( '과자', '국', '김치', '식용유')
    group by category
)
order by max_price desc