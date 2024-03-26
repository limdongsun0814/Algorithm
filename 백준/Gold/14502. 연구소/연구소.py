import copy
def bfs(pos1,pos2,pos3,mapArr,stack,movement,N,M):
    mapArr[pos1[0]][pos1[1]]=1
    mapArr[pos2[0]][pos2[1]]=1
    mapArr[pos3[0]][pos3[1]]=1
    while len(stack)>0:
        value = stack.pop(0)
        for move in movement:
            nextValue = [value[0]+move[0],value[1]+move[1]]
            if nextValue[0] <N and nextValue[1]<M and nextValue[0] >= 0 and nextValue[1] >= 0 and mapArr[nextValue[0]][nextValue[1]]==0:
                stack.append(nextValue)
                mapArr[nextValue[0]][nextValue[1]] =2
    return mapArr
def  findStack(mapArr):
    stack = []
    for i in range(len(mapArr)):
        for j in range(len(mapArr[i])):
            if mapArr[i][j]==2:
                stack.append([i,j])
    return stack

def findZ(mapArr):
    cnt = 0
    for i in range(len(mapArr)):
        for j in range(len(mapArr[i])):
            if mapArr[i][j]==0:
                cnt+=1
    return cnt
N,M = map(int,input().split())
mapArr = []
movement = [[1,0],[-1,0],[0,1],[0,-1]]
for i in range(N):
    mapArr.append(list(map(int,input().split())))
stack=findStack(mapArr)
cntArr =[]
for i in range(N*M):
    for j in range(i+1,N*M):
        for k in range(j+1,N*M):
            pos1 = [i//M,i%M]
            pos2 = [j//M,j%M]
            pos3 = [k//M,k%M]
            if mapArr[pos1[0]][pos1[1]]==0 and mapArr[pos2[0]][pos2[1]]==0 and mapArr[pos3[0]][pos3[1]]==0:
                copyMap = copy.deepcopy(mapArr)
                copyStack = copy.deepcopy(stack)
                copyMap = bfs(pos1,pos2,pos3,copyMap,copyStack,movement,N,M)
                cnt=findZ(copyMap)
                cntArr.append(cnt)
print(max(cntArr))