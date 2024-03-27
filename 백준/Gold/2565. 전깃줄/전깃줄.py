N = int(input())
arr =[]
keySet = []
for i in range(N):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:x[0])
dpM=[1]*N
for i in range(1,N):
    for j in range(i):
        if arr[j][1]<arr[i][1]:
            dpM[i]=max(dpM[i],dpM[j]+1)
print(N-max(dpM))