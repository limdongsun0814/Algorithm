n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort(key=lambda x:-x)
cnt = 0
ans=0
for i in arr:
    cnt+=1
    if cnt % 3 !=0:
        ans+=i
print(ans)