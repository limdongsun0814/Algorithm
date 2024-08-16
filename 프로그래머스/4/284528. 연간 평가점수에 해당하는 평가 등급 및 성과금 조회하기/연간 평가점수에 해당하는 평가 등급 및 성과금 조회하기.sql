select EMP_NO,EMP_NAME,GRADE,
case
    when GRADE="S" then 0.2*SAL
    when GRADE="A" then 0.15*SAL
    when GRADE="B" then 0.1*SAL
    else 0
end BONUS
from HR_EMPLOYEES join 
(select emp_no,
case
    when avg(score) >=96 then "S"
    when avg(score) >=90 then "A"
    when avg(score) >=80 then "B"
    else "C"
end GRADE
from HR_GRADE 
group by emp_no) A using(emp_no)