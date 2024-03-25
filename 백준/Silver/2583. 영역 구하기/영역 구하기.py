import sys
sys.setrecursionlimit(10**5)

def dfs(x,y):
    global cnt
    for move in movement:
        nextX = x+move[0]
        nextY = y+move[1]
        if nextX <N and nextX>=0 and nextY <M and nextY >=0 and visit[nextX][nextY]:
            visit[nextX][nextY]=False
            cnt+=1
            dfs(nextX,nextY)
M,N,K = map(int,input().split())
visit = [[True for i in range(M)]for j in range(N)]
for _ in range(K):
    xMin,yMin,xMax,yMax = map(int,input().split())
    for i in range(xMin,xMax):
        for j in range(yMin,yMax):
            visit[i][j]=False
movement = [[1,0],[-1,0],[0,1],[0,-1]]

arr = []
global cnt
for i in range(N):
    for j in range(M):
        if visit[i][j]:
            cnt=0
            visit[i][j]=False
            dfs(i,j)
            arr.append(cnt+1)
arr.sort()
strValue = ""
for i in arr:
    strValue+=str(i)+" "
print(len(arr))
print(strValue)