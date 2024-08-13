select concat("/home/grep/src/",maxval.board_id,"/",FILE_ID,FILE_NAME,FILE_EXT)  FILE_PATH
from USED_GOODS_FILE  ,( select board_id from used_goods_board order by VIEWS desc limit 1 )as maxval
where maxval.board_id=USED_GOODS_FILE.board_id
order by FILE_ID desc