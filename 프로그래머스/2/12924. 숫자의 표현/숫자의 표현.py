import collections 
def solution(n):
    answer = 0
    stack = collections.deque()
    value = 0
    for i in range(1,n+1):
        stack.append(i)
        value+=i
        while value>n:
            value-=stack.popleft()
        if value == n:
            answer+=1
    return answer