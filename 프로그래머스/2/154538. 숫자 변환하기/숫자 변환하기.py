def solution(x, y, n):
    answer = -1
    dpM = [0 for i in range(y+1)]
    dpM[x]=1
    for i in range(x+1,y+1):
        if i - n >= x and dpM[i - n] != 0:
            if dpM[i]!=0: 
                dpM[i]=min(dpM[i],dpM[i-n]+1)
            else:
                dpM[i]=dpM[i-n]+1
                
        if i%2==0 and dpM[i//2]!=0: #and i//2>=x
            if dpM[i]!=0:
                dpM[i]=min(dpM[i],dpM[i//2]+1)
            else:
                dpM[i]=dpM[i//2]+1
                
        if i%3==0 and dpM[i//3]!=0: #and i//3>=x
            if dpM[i]!=0: 
                dpM[i]=min(dpM[i],dpM[i//3]+1)
            else:
                dpM[i]=dpM[i//3]+1
    if dpM[y] !=0:
        answer=dpM[y]-1
    return answer
