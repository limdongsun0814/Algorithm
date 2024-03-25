def makeG(n,wires):
    g = {}
    for w in wires:
        if w[0] not in g:
            g[w[0]]=[]
        g[w[0]].append(w[1])
        if w[1] not in g:
            g[w[1]]=[]
        g[w[1]].append(w[0])
    return g
def bfs(g,value,n):
    cnt = 0
    stack = [value]
    visit = [True]*(n+1)
    visit[value]=False
    while len(stack)>0:
        val = stack.pop(0)
        cnt+=1
        for i in g[val]:
            if visit[i]:
                visit[i]=False
                stack.append(i)
    return cnt


def solution(n, wires):
    answer = -1
    g=makeG(n,wires)
    for w in wires:
        g[w[0]].remove(w[1])
        g[w[1]].remove(w[0])
        cnt1=bfs(g,w[0],n)
        cnt2=n-cnt1
        if answer<min(cnt1,cnt2):
            answer=min(cnt1,cnt2)
        g[w[0]].append(w[1])
        g[w[1]].append(w[0])
    return n-2*answer