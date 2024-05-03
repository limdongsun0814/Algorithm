def dp(index,start):
    if index>0:
        for i in range(start,start+1+(index-1)*4):
            arr[(n-index)*2][i]="*"
        
        for i in range(start,start+1+(index-1)*4):
            arr[i][(n-index)*2]="*"

        for i in range(start,start+1+(index-1)*4):
            arr[i][-((n-index)*2+1)]="*"

        for i in range(start,start+1+(index-1)*4):
            arr[-((n-index)*2+1)][i]="*"
        dp(index-1,start+2)

n = int(input())

arr = [[" " for i in range(1+(n-1)*4)] for i in range(1+(n-1)*4)]
m=1+(n-1)*4

dp(n,0)
for i in arr:
    for j in i:
        print(j,end="")
    print()