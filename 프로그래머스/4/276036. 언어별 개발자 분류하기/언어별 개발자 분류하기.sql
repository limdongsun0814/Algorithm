select * from (
select 
case
when SKILL_CODE & (select code from SKILLCODES where name="Python") = 
(select code from SKILLCODES where name="Python") and 
bin(skill_code & (select sum(code) from skillcodes where category="Front End")) like ("%1%") then "A"
when SKILL_CODE & (select code from SKILLCODES where name="C#") = 
(select code from SKILLCODES where name="C#") then "B"
when bin(skill_code & (select sum(code) from skillcodes where category="Front End")) like ("%1%") then "C"
end GRADE,
ID,EMAIL from DEVELOPERS 
) A
where A.GRADE is not null
order by 1,2
