import collections
def solution(order):
    answer = 0
    stack = collections.deque()
    arr = [ i for i in range(len(order),0,-1)]
    
    while len(arr)>0 or len(stack)>0:
        if len(arr)>0 and arr[-1] <=order[answer]:
            stack.append(arr.pop())
        else:
            if stack[-1]==order[answer]:
                stack.pop()
                answer+=1
            else:
                break
    
    return answer