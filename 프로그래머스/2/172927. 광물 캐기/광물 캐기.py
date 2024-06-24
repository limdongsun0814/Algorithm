def solution(picks, minerals):
    global answer
    answer = 25*1000
    miner = {}
    cnt=0
    for mineral in minerals:
        if cnt//5 not in miner:
            miner[cnt//5]={"diamond":0,"iron":0,"stone":0}
        miner[cnt//5][mineral]+=1
        cnt+=1
    dfs(0,picks,minerals,0,miner)
    return answer

def dfs(index,picks,minerals,value,miner):
    if index*5 >= len(minerals) or sum(picks)==0:
        global answer
        answer = min(answer, value)
        return
    if picks[0]>0:
        picks[0]-=1
        val = miner[index]["diamond"]+miner[index]["iron"]+miner[index]["stone"]
        dfs(index+1,picks,minerals,value+val,miner)
        picks[0]+=1
    
    if picks[1]>0:
        picks[1]-=1
        val = miner[index]["diamond"]*5+miner[index]["iron"]+miner[index]["stone"]
        dfs(index+1,picks,minerals,value+val,miner)
        picks[1]+=1
    
    if picks[2]>0:
        picks[2]-=1
        val = miner[index]["diamond"]*25+miner[index]["iron"]*5+miner[index]["stone"]
        dfs(index+1,picks,minerals,value+val,miner)
        picks[2]+=1
        
    