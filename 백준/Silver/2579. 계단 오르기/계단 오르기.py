def dp(index,cnt):
    if index < 0:
        return 0
    if dpM[cnt][index]!=0:
        return dpM[cnt][index]
    flog = []

    if cnt+1<2:
        flog.append(dp(index-1,cnt+1))
    flog.append(dp(index-2,0))
    dpM[cnt][index]=max(flog)+arr[index]
    return dpM[cnt][index]

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
dpM = [[0 for i in range(n)] for j in range(2)]
dpM[0][0]=arr[0]

result=dp(n-1,0)

print(result)