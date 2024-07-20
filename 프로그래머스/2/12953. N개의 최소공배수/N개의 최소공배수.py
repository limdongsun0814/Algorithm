import heapq
def solution(arr):
    answer = 0
    q = []
    for i in arr:
        heapq.heappush(q,[i,i])
    target = len(arr)
    cnt=0
    val=0
    while True:
        value = heapq.heappop(q)
        if value[0]!=val:
            val=value[0]
            cnt=0
        else:
            cnt+=1
        
        if cnt +1 == target:
            return val
        else:
            heapq.heappush(q,[value[0]+value[1],value[1]])
    return answer