select dept_id,DEPT_NAME_EN,round(avg(sal),0) avg_sal from HR_EMPLOYEES join HR_DEPARTMENT using(dept_id)
group by dept_id
order by avg_sal desc