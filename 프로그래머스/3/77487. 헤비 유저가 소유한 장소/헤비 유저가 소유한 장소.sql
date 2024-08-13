select places.* from places join
(select host_id, count(*) cnt from places group by host_id having cnt>=2) big using(host_id) order by id