select AUTHOR_ID,author_name,CATEGORY,sum(SALES*PRICE) TOTAL_SALES
from  BOOK join author using(author_id)
join BOOK_SALES using(BOOK_ID)
where date_format(SALES_DATE,'%Y%m')='202201'
group by AUTHOR_ID,CATEGORY
order by AUTHOR_ID,CATEGORY desc