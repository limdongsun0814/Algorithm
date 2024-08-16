select ID,EMAIL,FIRST_NAME,LAST_NAME from DEVELOPERS 
where bin(SKILL_CODE & (select sum(code) from SKILLCODES where category = "Front End")) like ("%1%")
order by 1