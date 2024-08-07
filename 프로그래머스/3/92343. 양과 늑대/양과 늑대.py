def solution(info, edges):
    answer = 0
    g = makeG(edges)
    global result
    result = 0
    for init in range(1):
        visit = [[[True]*(len(info)+1) for i in range(len(info)+1)] for j in range(len(info))]
        if info[init]==0:
            info[init]=2
            dfs(g,visit,info,[init,1,0])
            info[init]=0
        else:
            info[init]=2
            dfs(g,visit,info,[init,0,1])
            info[init]=1
    return result

def makeG(edges):
    g = {}
    for edge in edges:
        if edge[0] not in g:
            g[edge[0]]=[]
        if edge[1] not in g:
            g[edge[1]]=[]
        
        g[edge[0]].append(edge[1])
        g[edge[1]].append(edge[0])
    return g

def dfs(g,visit,info,value):
    global result
    if result < value[1]:
        result=value[1]
    
    for i in g[value[0]]:
        if visit[i][value[1]][value[2]]:
            visit[i][value[1]][value[2]]=False
            if info[i] == 0:
                info[i]=2
                dfs(g,visit,info,[i,value[1]+1,value[2]])
                info[i]=0
            elif info[i]==1 and value[1]>value[2]+1:
                info[i]=2
                dfs(g,visit,info,[i,value[1],value[2]+1])
                info[i]=1
            elif info[i]==2:
                dfs(g,visit,info,[i,value[1],value[2]])
                
            visit[i][value[1]][value[2]]=True
    
    
    
    
    