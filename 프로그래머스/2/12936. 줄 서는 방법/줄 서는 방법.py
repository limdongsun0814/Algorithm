import collections
def solution(n, k):
    answer = []
    value = 1
    arr = [] 
    arr.append(1)
    for i in range(2,n+1):
        value *= i
        arr.append(i)
    # stack.append(n)
    k-=1
    while len(answer)!=n:
        stack = collections.deque(arr)
        value=value//len(stack)
        # print(value,k,stack)
        for i in range(k//value):
            stack.append(stack.popleft())
        answer.append(stack.popleft())
        k=k%value
        arr.remove(answer[-1])
        # print(k)
        
    return answer
# [1,2,3] = > [3,1,2]