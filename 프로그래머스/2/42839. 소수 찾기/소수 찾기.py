import copy
def dfs(using,value):
    global dic, n, arr
    if value != "":
        dic[int(value)]=True
    for i in range(n):
        if using[i]:
            newUsing = copy.deepcopy(using)
            newUsing[i]=False
            dfs(newUsing,value+arr[i])


def solution(numbers):
    answer = 0
    global dic, n, arr
    arr = numbers
    n = len(numbers)
    dic = {}
    using = [True]*n
    dfs(using,"")
    for i in dic:
        for j in range(2,int(i**0.5)+1):
            if i % j==0:
                dic[i]=False
                break
    for i in dic:
        if dic[i] and i > 1:
            answer+=1
    return answer