def solution(n):
    answer = 0
    if n % 2 ==1:
        return 0
    if n == 2:
        return 3
    if n == 4:
        return 11
    
    dpM=[0]*n
    dpM[1]=3
    dpM[3]=11
    
    for i in range(5,n,2):
        dpM[i]=((dpM[i-2]*4)%1000000007-dpM[i-4]%1000000007+1000000007)%1000000007
        
    return dpM[-1]