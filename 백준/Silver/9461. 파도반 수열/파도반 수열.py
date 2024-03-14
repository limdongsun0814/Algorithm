def dp(N):
    if dpM[N] != None:
        return dpM[N]
    dpM[N] = dp(N-3) + dp(N-2)
    return dpM[N]

T = int(input())

for tttt in range(T):
    n = int(input())
    dpM = [None for i in range(101)]
    dpM[0]=1
    dpM[1]=1
    dpM[2]=1

    result=dp(n-1)
    print(result)