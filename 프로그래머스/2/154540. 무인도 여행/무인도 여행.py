def solution(maps):
    answer = []
    movement = [[1,0],[-1,0],[0,1],[0,-1]]
    n,m=len(maps),len(maps[0])
    visit = [[True for i in range(m)]for j in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j]!="X" and visit[i][j]:
                stack = [[i,j]]
                size = int(maps[i][j])
                visit[i][j]=False
                
                while len(stack)>0:
                    value=stack.pop(0)
                    for move in movement:
                        newValue = [value[0]+move[0],value[1]+move[1]]
                        if newValue[0] >=0 and newValue[1] >=0 and newValue[0]<n and newValue[1]<m and visit[newValue[0]][newValue[1]] and maps[newValue[0]][newValue[1]]!="X":
                            stack.append(newValue)
                            size+=int(maps[newValue[0]][newValue[1]])
                            visit[newValue[0]][newValue[1]]=False
                answer.append(size)
    if len(answer)==0:
        answer.append(-1)
    answer.sort()
    return answer