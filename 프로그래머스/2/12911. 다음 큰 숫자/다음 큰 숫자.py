import sys
def solution(n):
    answer=0
    cnt = bin(n).count("1")
    for i in range(n+1,1000001):
        if bin(i).count("1")==cnt:
            return i
    return answer

            
        
    
    
    