import collections
def solution(elements):
    answer = 0
    arr = collections.deque(elements)
    value = set()

    for i in elements:
        value.add(i)
    
    for i in range(2,len(elements)):
        sumValue = sum(elements[len(elements)-i:])  
        stack = collections.deque(elements[len(elements)-i:])
        for _ in range(len(elements)):
            value.add(sumValue)
            element=arr.popleft()
            stack.append(element)
            sumValue+=element
            sumValue-=stack.popleft()
            arr.append(element)
    value.add(sum(elements))
    return len(value)