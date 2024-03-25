import copy
def dfs(visit,k,cnt):
    global arr,maxValue

    if maxValue <cnt:
        maxValue=cnt

    for i in range(len(arr)):
        if visit[i]==False and arr[i][0]<=k:
            newVisit=copy.deepcopy(visit)
            newVisit[i]=True
            dfs(newVisit,k-arr[i][1],cnt+1)


def solution(k, dungeons):
    global arr,maxValue
    arr = dungeons
    visit=[False]*len(dungeons)
    maxValue = 0
    dfs(visit,k,0)
    answer = maxValue
    return answer