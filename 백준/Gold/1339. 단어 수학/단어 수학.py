N = int(input())
arr = []
maxSize = 0
keySet = {}
for i in range(N):
    arr.append(input())
    for j in arr[i]:
        keySet[j]=-1
    if maxSize < len(arr[i]):
        maxSize=len(arr[i])
# print(arr,maxSize)
arr2 =[]
for i in range(maxSize,0,-1):
    flog = []
    for value in arr:
        if i<=len(value):
            flog.append(value[len(value)-i])
    arr2.append(flog)
# print(arr2)
# print(keySet)
arr3 = []
for key in keySet:
    total = 0
    for i in arr:
        value = ""
        for j in i:
            if j==key:
                value+="1"
            else:
                value+="0"
        total+=int(value)
    arr3.append([key,total])
arr3.sort(key=lambda x: -x[1])
# print(arr3)
cnt = 9
for i in arr3:
    keySet[i[0]]=cnt
    cnt-=1
# print(keySet)
sum = 0
for i in arr:
    flog = ""
    for j in i:
        flog+=str(keySet[j])
    sum+=int(flog)
print(sum)