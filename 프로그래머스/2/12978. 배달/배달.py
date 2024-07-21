import collections
def solution(N, road, K):

    g=makeG(road)
    
    stack = collections.deque()
    # visit = [[False for i in range(N+1)]for j in range(N+1)]
    visit = [50*2000001]*(N+1)
    stack.append([1,0])
    visit[1] = 0
    
    
    answer = bfs(stack,visit,g,K)
    return answer

def makeG(road):
    dic = {}
    for i in road:
        if i[0] not in dic:
            dic[i[0]]=[]
        if i[1] not in dic:
            dic[i[1]]=[]
            
        dic[i[0]].append([i[1],i[2]])
        dic[i[1]].append([i[0],i[2]])
    return dic

def bfs(stack,visit,g,k):
    result = set()
    result.add(1)
    while len(stack) > 0:
        value = stack.popleft()
        for i in g[value[0]]:
            newValue = [i[0],value[1]+i[1]]
            if  visit[i[0]]>newValue[1] and newValue[1] <= k:
                stack.append(newValue)
                result.add(newValue[0])
                visit[i[0]]=newValue[1]
    return len(result)
            