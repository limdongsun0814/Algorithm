def dfs(n,r,c):
    global arr,index,targetR,targetC
    if n == 0:
        # print(index,r,c,targetR,targetC)
        # arr[r][c]=index
        print(index)
        exit()
        # arr[targetR][targetC]=index+(targetR-r)+(targetC-c)
        index+=1
    else:
        # print(index,r,c)
        if r<=targetR<r+2**(n-1) and c<=targetC<c+2**(n-1):
            dfs(n-1,r,c)
        else:
            index+=4**(n-1)
        if r<=targetR<r+2**(n-1) and c+2**(n-1)<=targetC<c+2**(n):
            dfs(n-1,r,c+2**(n-1))
        else:
            index+=4**(n-1)
        if r+2**(n-1)<=targetR<r+2**(n) and c<=targetC<c+2**(n-1):
            dfs(n-1,r+2**(n-1),c)
        else:
            index+=4**(n-1)
        if r+2**(n-1)<=targetR<r+2**(n) and c+2**(n-1)<=targetC<c+2**(n):
            dfs(n-1,r+2**(n-1),c+2**(n-1))

global arr,index,targetR,targetC

n,targetR,targetC = map(int,input().split())
# arr = [[-1 for i in range(2**n)] for j in range(2**n)]
index=0
# print(arr)
dfs(n,0,0)