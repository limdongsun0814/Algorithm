n,m = map(int,input().split())
robot =list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
cnt = 0
movement= [[-1,0],[0,1],[1,0],[0,-1]]
robot[2]=movement[robot[2]]
# 1 1 1
# 1 0 1
# 0 1 1

# 1 0 =>
while True:
    if arr[robot[0]][robot[1]]==0:
        cnt+=1
        arr[robot[0]][robot[1]]=2
    flog = True
    for move in movement:
        nextX=robot[0]+move[0]
        nextY=robot[1]+move[1]
        if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m and arr[nextX][nextY]==0:
            flog=False
            break
    if flog:
        robot[0]-=robot[2][0]
        robot[1]-=robot[2][1]
        if robot[0] < 0 or robot[0] >= n or robot[1] < 0 or robot[1] >= m or arr[robot[0]][robot[1]]==1:
            print(cnt)
            break
    else:
        while True:
            moveing = [-robot[2][1], robot[2][0]]
            nextX=robot[0]+moveing[0]
            nextY=robot[1]+moveing[1]
            robot[2]=moveing
            if nextX >= 0 and nextX < n and nextY >= 0 and nextY < m and arr[nextX][nextY]==0:
                robot[0]=nextX
                robot[1]=nextY
                break