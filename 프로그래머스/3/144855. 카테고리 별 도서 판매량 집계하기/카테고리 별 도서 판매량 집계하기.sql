select category, sum(cnt) total_sales from book
join (
select book_id,sum(SALES) cnt from BOOK_SALES 
where date_format(sales_date,'%y%m')="2201"
group by book_id) A using(book_id)
group by category
order by 1