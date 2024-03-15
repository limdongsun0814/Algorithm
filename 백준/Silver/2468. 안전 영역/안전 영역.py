def makeMap(arr,n,h):
    mapArr = []
    for i in range(n):
        flog = []
        for j in range(n):
            if arr[i][j]>h:
                flog.append(False)
            else:
                flog.append(True)
        mapArr.append(flog)
    return mapArr

def bfs(val):
    global movement, mapArr
    stack = []
    stack.append([val[0],val[1]])
    mapArr[val[0]][val[1]]=True

    while len(stack)>0:
        val=stack.pop(0)
        for move in movement:
            nextVal = [val[0]+move[0],val[1]+move[1]]
            if nextVal[0] >=0 and nextVal[1]>=0 and nextVal[0]<n and nextVal[1]<n:
                if mapArr[nextVal[0]][nextVal[1]] == False:
                    mapArr[nextVal[0]][nextVal[1]]=True
                    stack.append(nextVal)

global movement,n
movement = [[1,0],[-1,0],[0,1],[0,-1]]
n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
# print(arr)

minH = 101
maxH = 0
for i in range(n):
    for j in range(n):
        if minH > arr[i][j]:
            minH = arr[i][j]
        if maxH < arr[i][j]:
            maxH = arr[i][j]
# print(minH,maxH)
cntArr = []
for i in range(minH-1,maxH):
    global mapArr
    mapArr=makeMap(arr,n,i)
    cnt = 0
    for j in range(n):
        for k in range(n):
            if mapArr[j][k]==False:
                bfs([j,k])
                cnt+=1
    cntArr.append(cnt)
print(max(cntArr))