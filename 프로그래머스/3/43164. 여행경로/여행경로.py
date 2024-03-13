def makeG(tockets):
    g = {}
    for i in tockets:
        if i[0] not in g:
            g[i[0]] = []
        g[i[0]].append(i[1])

    for i in g:
        g[i].sort()
    return g

def dfs(g,value,arr,cnt,target):
    global result, flag
    nextArr = arr + [value]
    if cnt == target and flag:
        flag = False
        result.append(nextArr)
        return nextArr
    elif cnt == target:
        return
    if value in g:
        for i in g[value]:
            nextValue=g[value].pop(0)
            dfs(g,nextValue,nextArr,cnt+1,target)
            g[value].append(i)


def solution(tickets):
    global result,flag
    result = []
    g=makeG(tickets)
    print(g)
    arr=[]
    flag = True
    dfs(g,"ICN",arr,0,len(tickets))
    for i in result:
        print(i)
    answer = result[0]
    return answer