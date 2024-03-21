import heapq

def solution(scoville, K):
    answer = -1
    arr = []
    for i in scoville:
        heapq.heappush(arr, i)
    cnt = 0
    while arr[0]<K:
        if len(arr)<=1:
            return -1
        else:
            first = heapq.heappop(arr)
            last = heapq.heappop(arr)
            value = first + last + last
            cnt += 1
            heapq.heappush(arr,value)
    return cnt