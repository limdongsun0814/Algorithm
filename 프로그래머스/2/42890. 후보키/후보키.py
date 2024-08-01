import collections
def solution(relation):
    global answer
    tree=set(range(len(relation[0])))
    answer = 0
    return bfs(relation)

def bfs(relation):
    result = 0
    stack = collections.deque()
    memo = set()
    for i in range(len(relation[0])):
        stack.append([set([i]),i])

    while len(stack)>0:
        value = stack.popleft()
        if check(relation,value[0]):
            flag1 = True
            for i in memo:
                flag = True
                for j in i:
                    if j not in value[0]:
                        flag=False
                if flag:
                    flag1=False
                    break
            if flag1:
                result+=1
                memo.add(tuple(value[0]))
            #     print(value[0])
            # print(value[0],'aaa')
        else:
            for i in range(value[1]+1,len(relation[0])):
                newValue = [set(list(value[0])),i]
                newValue[0].add(i)
                stack.append(newValue)
    return result
            
def check(relation,index):
    arr = set()
    for data in relation:
        flag = []
        for i in index:
            flag.append(data[i])
        flag = tuple(flag)
        if flag not in arr:
            arr.add(flag)
        else:
            return False
    return True