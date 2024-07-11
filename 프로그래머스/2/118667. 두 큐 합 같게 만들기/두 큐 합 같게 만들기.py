import collections
def solution(queue1, queue2):
    answer = 0
    queVal1 = sum(queue1)
    queVal2 = sum(queue2)
    target = (queVal1+queVal2)//2
    arr1 = collections.deque(queue1)
    arr2 = collections.deque(queue2)
    n = len(arr1)+len(arr2)

    while queVal1 != target:
        if queVal1 > target:
            val=arr1.popleft()
            queVal1-=val
            arr2.append(val)
            queVal2+=val
        else:
            val=arr2.popleft()
            queVal2-=val
            arr1.append(val)
            queVal1+=val
        answer+=1
        if answer>n+n:
            answer=-1
            break
            
            
    return answer