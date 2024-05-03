n,m = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
maxValue=0
argmax=0
for i in arr:
    if i > maxValue:
        maxValue=i
        argmax=cnt
    cnt+=1

arr1 = arr[:argmax]
arr2 = arr[argmax:]
arr2.pop(0)

ans = 0
maxValue2 = 0
for i in arr1:
    if maxValue2<i:
        maxValue2=i
    else:
        ans+=maxValue2-i
arr2.reverse()

maxValue2 = 0
for i in arr2:
    if maxValue2<i:
        maxValue2=i
    else:
        ans+=maxValue2-i
print(ans)