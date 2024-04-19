def solution(maps):
    answer = 0
    flagS =True
    flagE = True

    movement=[[1,0],[-1,0],[0,-1],[0,1]]
    visit = []
    xSize=len(maps)
    ySize=len(maps[0])
    for i in range(len(maps)):
        flag = []
        for j in range(len(maps[i])):
            flag.append(True)
            if maps[i][j]=="L":
                start=[i,j,0]
        visit.append(flag)

    visit[start[0]][start[1]] = False
    stack = [start]

    while len(stack)>0:
        value=stack.pop(0)
        if maps[value[0]][value[1]]=="S" and flagS:
            answer+=value[2]
            flagS=False
        if maps[value[0]][value[1]]=="E" and flagE:
            answer+=value[2]
            flagE=False

        for move in movement:
            nextValue=[value[0]+move[0],value[1]+move[1],value[2]+1]
            if nextValue[0]>=0 and nextValue[1]>=0 and nextValue[0]<xSize and nextValue[1]<ySize and visit[nextValue[0]][nextValue[1]] and maps[nextValue[0]][nextValue[1]]!="X":
                visit[nextValue[0]][nextValue[1]]=False
                stack.append(nextValue)
    if flagS or flagE:
        answer=-1
    return answer