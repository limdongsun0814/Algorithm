def dfs(value,x,y):
    if value<3:
        return
    for i in range(3):
        for j in range(3):
            if i!=1 or j != 1:
                dfs(value//3,i*(value//3)+x,j*(value//3)+y)
            else:
                for ii in range(value//3+x,2*(value//3)+x):
                    for jj in range(value//3+y,2*(value//3)+y):
                        arr[ii][jj]=" "
    



n = int(input())
arr = [["*" for i in range(n)] for j in range(n)]

dfs(n,0,0)

for i in arr:
    for j in i:
        print(j,end="")
    print()