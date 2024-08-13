select USER_ID, NICKNAME,concat(city," ",STREET_ADDRESS1," ",STREET_ADDRESS2) 전체주소, 
concat(substring(TLNO,1,3),"-",substring(tlno,4,4),"-",substring(tlno,8,4)) 전화번호
from used_goods_user join (select writer_id user_id,count(*) cnt from USED_GOODS_BOARD group by writer_id having cnt>=3) cnt using(user_id)
order by 1 desc