def solution(n, results):
    answer = 0
    winG,g=makeG(n,results)
    # print(winG,g)
    global visit
    for i in range(1,n+1):
        visit=[True]*(n)
        dfs(g,i)
        dfs(winG,i)
        visit[i-1]=False
        # print(visit)
        if True not in visit:
            answer+=1
    return answer

def dfs(g,value):
    global visit
    for i in g[value]:
        if visit[i-1]:
            visit[i-1]=False
            dfs(g,i)
            
def makeG(n,results):
    g,winG={},{}
    for i in range(1,n+1):
        g[i]=[]
        winG[i]=[]
        
    for result in results:
        winG[result[0]].append(result[1])
        g[result[1]].append(result[0])
    return winG,g