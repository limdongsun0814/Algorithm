n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

dpM = arr[0]# [0,0,0]

for index in range(1,n):
    flag = dpM[:]
    dpM[0]=arr[index][0]+min(flag[1],flag[2])
    dpM[1]=arr[index][1]+min(flag[0],flag[2])
    dpM[2]=arr[index][2]+min(flag[0],flag[1])

print(min(dpM))