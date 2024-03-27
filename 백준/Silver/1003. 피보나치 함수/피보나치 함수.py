arr = []
T = int(input())
for tttttt in range(T):
    N = int(input())
    dpM = [[0,0] for i in range(40+1)]
    dpM[0]=[1,0]
    dpM[1]=[0,1]
    for i in range(2,N+1):
        dpM[i][0]=dpM[i-1][0]+dpM[i-2][0]
        dpM[i][1]=dpM[i-1][1]+dpM[i-2][1]
    print(dpM[N][0],dpM[N][1])