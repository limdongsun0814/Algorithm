select B.YEAR,A.size-B.SIZE_OF_COLONY YEAR_DEV, B.ID from
(select *, Year(DIFFERENTIATION_DATE) YEAR from ECOLI_DATA B) B
join (select Year(DIFFERENTIATION_DATE) DIFFERENTIATION_DATE,
max(SIZE_OF_COLONY) size
from ECOLI_DATA 
group by Year(DIFFERENTIATION_DATE)) A
on(B.YEAR=A.DIFFERENTIATION_DATE)
order by YEAR,YEAR_DEV