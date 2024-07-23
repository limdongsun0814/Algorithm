def solution(n,a,b):
    answer = 0

    A = min(a,b)
    B = max(a,b)
    
    # a = (a-1)//2
    # print(a+1)
    
    while True:
        answer+=1
        if B-A==1 and A % 2 == 1:
            break
        B = (B-1)//2+1
        A = (A-1)//2+1
    return answer

# 2