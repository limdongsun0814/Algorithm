select MEMBER_NAME,REVIEW_TEXT,date_format(REVIEW_DATE,"%Y-%m-%d")  REVIEW_DATE  from MEMBER_PROFILE join REST_REVIEW using(member_id)
where member_id=(select member_id from rest_review group by member_id order by count(*) desc limit 1)
order by REVIEW_DATE,REVIEW_TEXT