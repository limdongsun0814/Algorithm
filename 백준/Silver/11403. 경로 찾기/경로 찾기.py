import heapq
n = int(input())

dic = {}

for i in range(n):
    arr = list(map(int,input().split()))
    dic[i]=[]
    for j in range(n):
        if arr[j]==1:
            dic[i].append(j)

# print(dic)

for i in range(n):
    visit = [False]*n
    stack = [i]
    # visit[i]=True
    arr = []
    while len(stack)>0:
        value = stack.pop(0)
        for j in dic[value]:
            if visit[j]==False:
                visit[j]=True
                stack.append(j)
                heapq.heappush(arr,j)
    # print(arr)
    heapq.heappush(arr,101)
    val = heapq.heappop(arr)
    for i in range(n):
        if val==i:
            print("1",end=" ")
            val = heapq.heappop(arr)
        else:
            print("0",end=" ")
    print()