import copy
N, K = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

dpM = []
for i in range(K+1):
    flog = [True]*N
    dpM.append([0,flog])


for i in range(1,K+1):
    maxValue = dpM[0][0]
    maxUsing = dpM[0][1]
    for j in range(len(arr)):
         if i >= arr[j][0]:
            # value =copy.deepcopy(dpM[i-arr[j][0]])
            # value =[item[:] for item in dpM[i-arr[j][0]]]
            value =[dpM[i-arr[j][0]][0],dpM[i-arr[j][0]][1][:]]
            if value[1][j]:
                value[1][j]=False
                # flog.append([value[0]+arr[j][1],value[1]])
                if maxValue < value[0]+arr[j][1]:
                    maxValue = value[0]+arr[j][1]
                    maxUsing = value[1]

    dpM[i]=[maxValue,maxUsing]
arr2 = []
for i in dpM:
    arr2.append(i[0])
print(max(arr2))