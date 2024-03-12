def solution(numbers, target):
    global cnt, l, arr, targetValue
    
    cnt=0
    l = len(numbers)
    arr = numbers
    targetValue = target
    
    dfs(0,0)
    
    answer = cnt
    return answer

def dfs(index,value):
    global cnt, l, arr, targetValue
    if index == l:
        if value==targetValue:
            cnt=cnt+1
            return
        else:
            return
    
    dfs(index+1,value+arr[index])
    dfs(index+1,value-arr[index])
    
    
        