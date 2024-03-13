def bfs(value,cnt):
    global stack, movement,answer,x,y,visit,mapArr
    if value[0] == x-1 and value[1] == y-1:
        del stack
        answer = cnt+1
        return

    for i in movement:
        newValue = [value[0]+i[0],value[1]+i[1]]
        if newValue[0] < x and newValue[1] < y and newValue[0] >=0 and newValue[1] >=0:
            if visit[newValue[0]][newValue[1]]==False and mapArr[newValue[0]][newValue[1]]==1:
                visit[newValue[0]][newValue[1]] = True
                stack.append([newValue,cnt+1])
    if len(stack)>0:
        print(len(stack))
        newValue1 = stack.pop(0)
        bfs(newValue1[0],newValue1[1])
        
def solution(maps):
    global stack, movement,answer,x,y,visit,mapArr

    visit = []
    stack = []
    mapArr = maps
    answer=-1
    movement = [[1,0],[-1,0],[0,1],[0,-1]]
    x = len(maps)
    y = len(maps[0])

    for i in range(len(maps)):
        visit.append([])
        for j in range(len(maps[i])):
            visit[i].append(False)
    visit[0][0]=True
    
    # bfs([0,0],0)
    
    stack.append([[0,0],0])
    while len(stack)>0:
        value1 = stack.pop(0)
        value = value1[0]
        cnt = value1[1]
        
        if value[0] == x-1 and value[1] == y-1:
            answer = cnt+1
            break

        for i in movement:
            newValue = [value[0]+i[0],value[1]+i[1]]
            if newValue[0] < x and newValue[1] < y and newValue[0] >=0 and newValue[1] >=0:
                if visit[newValue[0]][newValue[1]]==False and mapArr[newValue[0]][newValue[1]]==1:
                    visit[newValue[0]][newValue[1]] = True
                    stack.append([newValue,cnt+1])
        # if len(stack)>0:
        #     newValue1 = stack.pop(0)
    
    return answer