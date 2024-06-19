def solution(land):
    answer = 0
    n,m=len(land),len(land[0])
    arr = []
    for i in range(m):
        for j in range(n):
            if land[j][i]==1:
                flag=bfs(land,i,j,n,m)
                arr.append(flag)
    arr2 = [0 for i in range(m)]
    for i in arr:
        for j in range(i[1],i[2]+1):
            arr2[j]+=i[0]
    answer = max(arr2)
    return answer
def bfs(copyLand,i,j,n,m):
    stack = [[j,i]]
    copyLand[j][i]=0
    iMax = i
    iMin = i
    movement=[[1,0],[-1,0],[0,1],[0,-1]]
    cnt=1
    while len(stack)>0:
        value = stack.pop(0)
        for move in movement:
            newValue = [value[0]+move[0],value[1]+move[1]]
            if newValue[0] >= 0 and newValue[1] >= 0 and newValue[0] < n and newValue[1] < m:
                if copyLand[newValue[0]][newValue[1]]==1:
                    copyLand[newValue[0]][newValue[1]]=0
                    cnt+=1
                    stack.append(newValue)
                    iMax=max(iMax,newValue[1])
                    iMin=min(iMin,newValue[1])
    return [cnt,iMin,iMax]
                
    