import heapq
def solution(begin, end):
    answer = [0]*(end-begin+1)
    arr = []
    for i in range(end-begin+1):
        answer[i]=find(i+begin)
        
    return answer

def find(n):
    result = [1]
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            if n//i <= 10000000:
                return n//i
            if i <=10000000:
                result.append(i)
    if n == 1:
        return 0
    return max(result)
    # return 0