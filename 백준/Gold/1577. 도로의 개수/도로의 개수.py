n, m =map(int,input().split())
k=int(input())
arr = []
for i in range(k):
    arr.append(list(map(int,input().split())))

dpM = [[0 for i in range(n+1)] for j in range(m+1)]

dpM[0][0]=1

dic = {}
for i in arr:
    if (i[0],i[1]) not in dic:
        dic[i[0],i[1]]=[]
    dic[i[0],i[1]].append([i[2],i[3]])
    
    if (i[2],i[3]) not in dic:
        dic[i[2],i[3]]=[]
    dic[i[2],i[3]].append([i[0],i[1]])

movement=[[1,0],[0,1]]
for i in range(0,m+1):
    for j in range(0,n+1):
        for move in movement:
            if ((j,i) not in dic or [j+move[1],i+move[0]] not in dic[j,i]) and i+move[0]<=m and j+move[1]<=n:
                dpM[i+move[0]][j+move[1]]+=dpM[i][j]
print(dpM[m][n])  