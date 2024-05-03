N,K,A,B=map(int,input().split())

arr = [K]*N
day=0
cur = 0
while min(arr)-day>0:
    for i in range(A):
        arr[cur%N]+=B
        cur+=1
    day+=1
print(day)