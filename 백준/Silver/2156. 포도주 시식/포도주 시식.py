import sys
sys.setrecursionlimit(100000)
def dp(index,cnt):
    if index < 0:
        return 0
    if dpM[cnt][index]!=-1:
        return dpM[cnt][index]
    flog = []

    if cnt+1 <2:
        flog.append(dp(index-1,cnt+1)+arr[index])
    flog.append(dp(index-1,0))
    flog.append(dp(index - 2, 0)+ arr[index])
    dpM[cnt][index] = max(flog)
    return dpM[cnt][index]

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
dpM = [[-1 for i in range(n)] for j in range(2)]
dpM[0][0]=arr[0]

result=dp(n-1,0)

print(result)