select distinct ID, EMAIL, FIRST_NAME, LAST_NAME from DEVELOPERS,SKILLCODES 
where NAME in ("Python","C#") and SKILL_CODE & CODE = CODE
order by ID