def makeG(computers):
    global g
    for i in range(len(computers)):
        for j in range(len(computers)):
            g[i].append(computers[i][j])

def dfs(value):
    global visit,flag
    for i in range(len(g[value])):
        if g[value][i]==1 and visit[i]==False:
            flag = True
            visit[i]=True
            dfs(i)

def bfs(value):
    global visit, flag, stack

    for i in range(len(g[value])):
        if g[value][i] == 1 and visit[i] == False:
            stack.append(i)
            flag = True
            visit[i]=True

    if len(stack) > 0:
        bfs(stack.pop())
            
def solution(n, computers):
    global g,visit, cnt, flag, stack
    g = {}
    visit = []
    cnt = 0
    stack = []

    for i in range(n):
        g[i]=[]
        visit.append(False)

    makeG(computers)

    switch = True

    for i in range(n):
        flag = False
        if switch:
            dfs(i)
        else:
            stack.append(i)
            bfs(i)
        if flag:
            cnt+=1
    answer = cnt
    return answer
