import heapq
n= int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split()))) #시작 종료
arr.sort()
mapArr = [arr[0][1]]
for i in range(1,n):
    if arr[i][0]<mapArr[0]:
        heapq.heappush(mapArr,arr[i][1])
    else:
        heapq.heappop(mapArr)
        heapq.heappush(mapArr,arr[i][1])
print(len(mapArr))