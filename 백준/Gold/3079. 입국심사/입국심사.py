n,M = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
left = 0
right = max(arr)*M
result= max(arr)*M
while left<=right:
    m = (right+left)//2
    total = 0
    for i in arr:
        total+=m//i
    if total < M:
        left=m+1
    else:
        result=min(result,m)
        right=m-1
print(result)