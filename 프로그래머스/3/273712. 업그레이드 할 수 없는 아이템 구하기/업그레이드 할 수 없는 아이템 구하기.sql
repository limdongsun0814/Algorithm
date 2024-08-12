select ITEM_ID,ITEM_NAME,RARITY from ITEM_INFO 
where ITEM_ID not in (
select PARENT_ITEM_ID from ITEM_TREE where not(isnull(PARENT_ITEM_ID))
)
order by item_id desc