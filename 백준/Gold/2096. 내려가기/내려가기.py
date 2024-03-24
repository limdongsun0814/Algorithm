N =  int(input())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))
dpM=[[-1]*3 for j in range(N)]
dpM[0]=arr[0]

for i in range(1,N):
    dpM[i][0]=max( dpM[i-1][0]+arr[i][0], dpM[i-1][1]+arr[i][0])
    dpM[i][1]=max( dpM[i-1][0]+arr[i][1], dpM[i-1][1]+arr[i][1], dpM[i-1][2]+arr[i][1])
    dpM[i][2]=max(  dpM[i-1][1]+arr[i][2], dpM[i-1][2]+arr[i][2])
maxValue = max(dpM[N-1])
for i in range(1,N):
    dpM[i][0] = min(dpM[i - 1][0] + arr[i][0], dpM[i - 1][1] + arr[i][0])
    dpM[i][1] = min(dpM[i - 1][0] + arr[i][1], dpM[i - 1][1] + arr[i][1], dpM[i - 1][2] + arr[i][1])
    dpM[i][2] = min(dpM[i - 1][1] + arr[i][2], dpM[i - 1][2] + arr[i][2])
print(maxValue,min(dpM[N-1]))