select sum(SCORE) SCORE, EMP_NO, EMP_NAME, POSITION, EMAIL from
HR_EMPLOYEES join HR_GRADE using(EMP_NO)
where YEAR=2022
group by EMP_NO
order by score desc
limit 1