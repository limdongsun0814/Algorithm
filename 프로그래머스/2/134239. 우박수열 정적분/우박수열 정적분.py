def solution(k, ranges):
    answer = []
    arr = []
    while k != 1:
        if k % 2 == 0:
            flag = k//2
            value = (k-flag)/2+flag
        else:
            flag = k*3+1
            value = (flag-k)/2+k
        k=flag
        arr.append(value)
    n = len(arr)
    for i,j in ranges:
        if n-i+j>=0:
            value = 0
            for k in range(i,n+j):
                value+=arr[k]
            answer.append(value)
        else:
            answer.append(-1.0)
        
    return answer