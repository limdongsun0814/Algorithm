import heapq
def solution(n, k, enemy):
    answer = 0
    arr1 = []
    arr2 = []
    value = 0
    for i in range(len(enemy)):
        value+=enemy[i]
        heapq.heappush(arr1,-enemy[i])

        if value > n :
            flag = heapq.heappop(arr1)
            value+=flag
            heapq.heappush(arr2,flag)
            if len(arr2)> k:
                break
    # print(arr1,arr2)
    return len(arr1)+min(len(arr2),k)