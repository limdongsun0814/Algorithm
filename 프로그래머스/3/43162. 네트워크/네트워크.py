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
            
def solution(n, computers):
    global g,visit, cnt, flag
    g = {}
    visit = []
    cnt = 0
    for i in range(n):
        g[i]=[]
        visit.append(False)

    makeG(computers)

    for i in range(n):
        flag = False
        dfs(i)
        if flag:
            cnt+=1
    answer = cnt
    return answer