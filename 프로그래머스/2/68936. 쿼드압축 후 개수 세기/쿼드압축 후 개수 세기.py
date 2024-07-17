import numpy
def solution(arr):
    global answer
    answer = [0,0]
    arr = numpy.array(arr)
    deep(0,arr)
    
    return answer

def deep(deepCnt, arr):
    if check(arr):
        global answer
        answer[arr[0][0]]+=1
    else:
        n = arr.shape[0]
        deep(deepCnt+1,arr[:n//2,:n//2])
        deep(deepCnt+1,arr[n//2:,n//2:])
        deep(deepCnt+1,arr[:n//2,n//2:])
        deep(deepCnt+1,arr[n//2:,:n//2])
    
def check(arr):
    checkValue = arr[0][0]
    for i in arr:
        for j in i:
            if checkValue!=j:
                return False
    return True
    
