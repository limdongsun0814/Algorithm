import sys
sys.setrecursionlimit(10**5)
def dp(index):
    if index==0:
        return 0
    if index<0:
        return -1
    if dpM[index] != -1:
        return dpM[index]
    flog = [1000000]
    for i in arr:
        value = dp(index-i)+1
        if value !=0:
            flog.append(value)
    dpM[index]=min(flog)
    return dpM[index]


arr = []
n,k = map(int, input().split())
for i in range(n):
    arr.append(int(input()))
dpM=[-1 for i in range(k+1)]
result=dp(k)
if result !=1000000:
    print(result)
else:
    print(-1)