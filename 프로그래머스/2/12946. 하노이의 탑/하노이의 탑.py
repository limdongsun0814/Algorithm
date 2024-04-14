def move(start,to):
    global answer
    answer.append([start,to])

def dfs(index,start,to,via):
    if index==1:
        move(start,to)
    else:
        dfs(index-1,start,via,to)
        move(start,to)
        dfs(index-1,via,to,start)

def solution(n):
    global answer
    answer = []
    dfs(n,1,3,2)
    return answer
