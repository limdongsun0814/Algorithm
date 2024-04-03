import heapq

n=int(input())
arr = list(map(int,input().split()))
stack = [[arr[-1],n-1]]
heapq.heapify(stack)
result = [0]*n
for i in range(n-2,-1,-1):
    while len(stack)>0:
        value=heapq.heappop(stack)
        if arr[i]>=value[0]:
            result[value[1]]=i+1
        else:
            heapq.heappush(stack,value)
            break
    heapq.heappush(stack, [arr[i],i])
for i in result:
    print(i,end=" ")