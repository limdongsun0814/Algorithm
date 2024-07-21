def solution(n):
    answer = 0
    dpM = [0]*(n+1)
    dpM[0] = 0
    dpM[1] = 1
    for i in range(2,n+1):
        dpM[i]=(dpM[i-1]+dpM[i-2])%1234567
    # print(dpM)
    return dpM[-1]