select USER_ID,NICKNAME,price TOTAL_SALES from USED_GOODS_USER 
join (select WRITER_ID user_id, sum(price) price from used_goods_board where STATUS="DONE" group by user_id having price >= 700000) total_price using(user_id)
order by price