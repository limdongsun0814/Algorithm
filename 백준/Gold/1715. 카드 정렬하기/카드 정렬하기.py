import heapq
N = int(input())
arr = []
for i in range(N):
    heapq.heappush(arr,int(input()))
if N == 1 :
    print(0)
else:
    arr2 = []
    for i in range(1,N):
        # print(sumValue,arr[i])
        sumValue = heapq.heappop(arr) + heapq.heappop(arr)
        heapq.heappush(arr,sumValue)
        arr2.append(sumValue)
    print(sum(arr2))