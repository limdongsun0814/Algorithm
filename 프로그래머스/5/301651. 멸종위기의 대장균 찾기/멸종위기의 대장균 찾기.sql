with recursive ctr (id,parent_id,n) as (
    select id,parent_id,1
    from ecoli_data
    where parent_id is null
    union all
    select ecoli_data.id,ecoli_data.parent_id,ctr.n+1
    from ecoli_data join ctr on(ctr.id=ecoli_data.parent_id)
) 
select count(*) count,ctr.n GENERATION from ctr left join ecoli_data on(ctr.id=ecoli_data.parent_id)
where ecoli_data.parent_id is null
group by GENERATION
order by 2