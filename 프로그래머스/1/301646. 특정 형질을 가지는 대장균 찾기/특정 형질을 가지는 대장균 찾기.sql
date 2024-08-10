select count(*) COUNT from ECOLI_DATA 
where genotype&2=0 and genotype&5 in (1,4,5)

-- 1 0001 4 0100
