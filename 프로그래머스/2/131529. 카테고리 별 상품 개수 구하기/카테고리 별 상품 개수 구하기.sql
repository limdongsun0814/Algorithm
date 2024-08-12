select substring(PRODUCT_CODE,1,2) CATEGORY, count(*) products from product
group by CATEGORY
order by category