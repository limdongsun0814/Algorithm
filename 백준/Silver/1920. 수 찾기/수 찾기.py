input()
arr = list(map(int,input().split()))
input()
arr2 = list(map(int,input().split()))
arr.sort()
for target in arr2:
    left=0
    right=len(arr)-1
    flog=False
    while left<=right:
        m=(left+right)//2
        if arr[m]<target:
            left=m+1
        elif arr[m]==target:
            flog=True
            break
        else:
            right=m-1
    if flog:
        print(1)
    else:
        print(0)