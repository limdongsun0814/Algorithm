n = int(input())
arr=[]
for i in range(n):
    arr.append(list(input()))

movement = [[1,0],[-1,0],[0,1],[0,-1]]
visit = [[True for i in range(n)]for j in range(n)]
cnt=0
for i in range(n):
    for j in range(n):
        if visit[i][j]:
            cnt+=1
            stack=[]
            visit[i][j]=False
            check = arr[i][j]
            stack.append([i,j])
            while len(stack)>0:
                value=stack.pop(0)
                for move in movement:
                    nextValue = [value[0]+move[0],value[1]+move[1]]
                    if nextValue[0]>=0 and nextValue[0]<n and nextValue[1]>=0 and nextValue[1]<n and visit[nextValue[0]][nextValue[1]] and arr[nextValue[0]][nextValue[1]]==check:
                        visit[nextValue[0]][nextValue[1]]=False
                        stack.append(nextValue)
print(cnt,end=" ")

cnt=0
visit = [[True for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j]=="G":
            arr[i][j]="R"
for i in range(n):
    for j in range(n):
        if visit[i][j]:
            cnt+=1
            stack=[]
            visit[i][j]=False
            check = arr[i][j]
            stack.append([i,j])
            while len(stack)>0:
                value=stack.pop(0)
                for move in movement:
                    nextValue = [value[0]+move[0],value[1]+move[1]]
                    if nextValue[0]>=0 and nextValue[0]<n and nextValue[1]>=0 and nextValue[1]<n and visit[nextValue[0]][nextValue[1]] and arr[nextValue[0]][nextValue[1]]==check:
                        visit[nextValue[0]][nextValue[1]]=False
                        stack.append(nextValue)
print(cnt)