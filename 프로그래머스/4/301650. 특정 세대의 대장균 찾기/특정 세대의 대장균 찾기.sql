select C.ID from ECOLI_DATA A join ECOLI_DATA B on(A.ID=B.parent_id)
join ECOLI_DATA C on(B.ID=C.parent_id)
where A.PARENT_ID is null
order by C.id