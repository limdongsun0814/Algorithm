def solution(n):
    dpM = [1]*(n+1)
    
    for i in range(2,n+1):
        dpM[i]=(dpM[i-1]+dpM[i-2])%1234567
    return dpM[-1]