n,k = map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
value=0
cnt=0
arr.sort()
while value!=k:
    V = arr.pop()
    cnt+=(k-value)//V
    value+=((k-value)//V)*V
print(cnt)