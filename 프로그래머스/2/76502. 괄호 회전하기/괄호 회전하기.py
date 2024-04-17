def solution(s):
    arr = list(s)
    n=len(arr)
    answer = n
    dic = {"[":"]","{":"}","(":")"}
    for i in range(n):
        stack = []
        flag = True
        for j in arr:
            if j == "[" or j=="(" or j=="{":
                stack.append(j)
            elif len(stack)>0 and dic[stack[-1]]== j:
                stack.pop()
            else:
                answer-=1
                flag=False
                break
        if len(stack)>0 and flag:
            answer-=1
        arr.append(arr.pop(0))
    return answer