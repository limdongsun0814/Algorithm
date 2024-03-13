def makeG(begin,target,words):
    global g
    print(words)

    for i in range(len(words)):
        for j in range(len(words)):
            cnt = 0
            for A, B in zip(words[i],words[j]):
                if A != B:
                    cnt+=1
            if cnt == 1:
                g[i].append(j)

def bfs(stack,words,target,visit):
    global g
    while len(stack) > 0:
        value = stack.pop(0)

        if words[value[0]]==target:
            print(value[1])
            return value[1]

        for i in g[value[0]]:
            if visit[i] == False:
                visit[i]=True
                stack.append([i,value[1]+1])
    return 0
            
def solution(begin, target, words):
    global g,answer
    words.insert(0,begin)
    g = {}
    visit = []
    for i in range(len(words)):
        g[i]=[]
        visit.append(False)
    makeG(begin,target,words)
    print(g)

    stack = [[0,0]]
    answer=bfs(stack,words,target,visit)
    print(answer)
    return answer