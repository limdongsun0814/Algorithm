select ITEM_ID,ITEM_NAME from item_info join item_tree using(item_id)
where isnull(PARENT_ITEM_ID)
order by item_id