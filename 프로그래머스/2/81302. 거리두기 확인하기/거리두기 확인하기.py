def solution(places):
    answer = []
    for arr in places:
        if bfs(arr):
            answer.append(1)
        else:
            answer.append(0)
    return answer

def bfs(arr):
    stack = []
    visit = [[True for i in range(5)]for j in range(5)]
    movement = [[1,0],[-1,0],[0,1],[0,-1]]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]=='P':
                stack.append([i,j,0])
                visit[i][j]=False
                while len(stack)>0:
                    value=stack.pop(0)
                    if value[2]<2:
                        for move in movement:
                            newValue = [value[0]+move[0],value[1]+move[1],value[2]+1]
                            if newValue[0]>=0 and newValue[1]>=0 and newValue[0]<5 and newValue[1]<5 and visit[newValue[0]][newValue[1]]:
                                # print(arr[newValue[0]][newValue[1]],newValue)
                                if arr[newValue[0]][newValue[1]]=="P":
                                    return False
                                elif arr[newValue[0]][newValue[1]]!="X":
                                    visit[newValue[0]][newValue[1]]=False
                                    stack.append(newValue)
    
    
    return True
            