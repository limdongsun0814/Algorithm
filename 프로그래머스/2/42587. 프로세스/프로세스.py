import heapq
import collections
def solution(priorities, location):
    answer = 0
    arr = []
    q = collections.deque()
    for i in range(len(priorities)):
        heapq.heappush(arr,-priorities[i])
        q.append([priorities[i],i])
    print(q)
    while len(arr)>0 and len(q)>0:
        value=q.popleft()
        if value[0]==-arr[0]:
            heapq.heappop(arr)
            answer+=1
            if value[1]==location:
                break
        else:
            q.append(value)
    return answer