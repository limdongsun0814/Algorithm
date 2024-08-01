def solution(w,h):
    answer = 0
    flag = w
    w = min(h,flag)
    h = max(h,flag)
    value = 0
    
    for i in range(1,int(w**0.5)+1):
        if w % i == 0:
            n,m = i,w//i
            if h % n == 0 and value < n:
                value=n
            if h % m == 0 and value < m:
                value=m
    return w*h-(w+h-value)

