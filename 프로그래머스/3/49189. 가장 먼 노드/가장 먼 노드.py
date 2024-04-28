def  makeG(edge):
    dic={}
    for i in edge:
        if i[0] not in dic:
            dic[i[0]]=[]
        if i[1] not in dic:
            dic[i[1]]=[]

        dic[i[0]].append(i[1])
        dic[i[1]].append(i[0])
    return dic

def solution(n, edge):
    answer = 0
    cnt=0
    g=makeG(edge)


    stack=[[1,0]]
    visit = [True] * (n+1)
    visit[1]=False
    while len(stack)>0:
        value=stack.pop(0)

        if answer<value[1]:
            answer=value[1]
            cnt=1
        elif answer==value[1]:
            cnt+=1

        for nextValue in g[value[0]]:
            if visit[nextValue]:
                visit[nextValue]=False
                stack.append([nextValue,value[1]+1])

    return cnt