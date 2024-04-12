n = int(input())
arr = []
dpM = [0]*(n+1)

for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(1,n+1):
    dpM[i]=max(dpM[i-1],dpM[i])
    if i+arr[i-1][0]-1 <= n:
        dpM[i+arr[i-1][0]-1]=max(dpM[i-1]+arr[i-1][1],dpM[i+arr[i-1][0]-1])
print(dpM[n])