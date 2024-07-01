def solution(storey):
    global answer
    answer = 100000000
    n=len(str(storey))
    back(0,storey,0,n)
    return answer

def back(index,value,cnt,n):
    global answer
    if value==0:
        answer=min(answer,cnt)
        return
    if value==1:
        answer=min(answer,cnt+1)
        return
    back(index+1,value//10,cnt+value%10,n)
    back(index+1,value//10+1,cnt+10-value%10,n)