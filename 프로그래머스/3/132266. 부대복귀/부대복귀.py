import collections
def solution(n, roads, sources, destination):
    answer = []
    g = init(n,roads)
    # print(g)
    
    visit = [False for i in range(n+1)]
    visit[destination]=-1
    
    stack = collections.deque([[destination,0]])
    while len(stack)>0:
        value=stack.popleft()
        for newPose in g[value[0]]:
            if visit[newPose]==False:
                newValue = [newPose,value[1]+1]
                stack.append(newValue)
                visit[newValue[0]]=newValue[1]
    # print(visit)
    
    for i in sources:
        if visit[i]==False:
            answer.append(-1)
        elif visit[i]==-1:
            answer.append(0)
        else:
            answer.append(visit[i])
    
    return answer

def init(n,roads):
    g = {}
    for road in roads:
        if road[0] not in g:
            g[road[0]]=[]
        if road[1] not in g:
            g[road[1]]=[]
        
        g[road[0]].append(road[1])
        g[road[1]].append(road[0])
    return g
