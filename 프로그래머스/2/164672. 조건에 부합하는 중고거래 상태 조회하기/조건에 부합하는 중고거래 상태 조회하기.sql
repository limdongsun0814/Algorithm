select BOARD_ID,WRITER_ID,TITLE,PRICE,
case
when STATUS="SALE" then "판매중"
when STATUS="RESERVED" then "예약중"
when STATUS="DONE" then "거래완료"
end
from USED_GOODS_BOARD 
where CREATED_DATE="2022-10-05"
order by BOARD_ID desc