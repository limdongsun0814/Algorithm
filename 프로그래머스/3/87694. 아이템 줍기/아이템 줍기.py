def bfs(x,y,endX,endY,rectangle):
    stack = [[x,y,0]]
    visit = [[False for i in range(52)]for j in range(52)]
    movement = [[1,0],[-1,0],[0,1],[0,-1]]
    visit[x][y] = True
    while len(stack) > 0:
        value = stack.pop(0)
        nowX = value[0]
        nowY = value[1]
        cnt = value[2]

        if nowX == endX and nowY == endY:
            return cnt

        for i in rectangle:
            for j in movement:
                nextX = nowX+j[0]
                nextY = nowY+j[1]

                if nextX >0 and nextX <= 50:
                    if visit[nextX][nextY] == False and i[0] <= nextX and i[1] <= nextY and i[2] >= nextX and i[3] >= nextY:
                        if i[0] <= nowX and i[1] <= nowY and i[2] >= nowX and i[3] >= nowY:
                            flag = True
                            for k in rectangle:
                                if k[0] < nowX+j[0]*0.5 and k[1] < nowY+j[1]*0.5 and k[2] > nowX+j[0]*0.5 and k[3] > nowY+j[1]*0.5:
                                    # print(nextX,nextY)
                                    flag = False
                                    break
                            if flag:
                                visit[nextX][nextY] = True
                                stack.append([nextX,nextY,cnt+1])
    return 0


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = bfs(characterX,characterY,itemX,itemY,rectangle)
    return answer