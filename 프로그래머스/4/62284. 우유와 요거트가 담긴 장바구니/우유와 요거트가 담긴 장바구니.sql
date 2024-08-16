select CART_ID from CART_PRODUCTS 
where name="Milk" and cart_id in (select cart_id from CART_PRODUCTS where name = "Yogurt")
order by 1