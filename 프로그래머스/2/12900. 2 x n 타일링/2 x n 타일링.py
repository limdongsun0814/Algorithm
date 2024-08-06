def solution(n):
    answer = 0
    if n <=2:
        return n
    dpM=[0]*n
    dpM[0]=1
    dpM[1]=2
    for i in range(2,n):
        dpM[i]=(dpM[i-1]+dpM[i-2])%1000000007
    
    return dpM[-1]