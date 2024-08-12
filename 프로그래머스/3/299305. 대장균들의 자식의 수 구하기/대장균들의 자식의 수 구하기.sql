select B.ID,count(A.ID) CHILD_COUNT from ECOLI_DATA A right join ECOLI_DATA B on(A.PARENT_ID=B.ID)
group by B.ID
order by 1