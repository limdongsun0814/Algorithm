def solution(sequence, k):
    answer = []
    start, end = 0,0
    val = 0
    arr = []
    while start != len(sequence):
        val+=sequence[start]
        start+=1
        
        if val > k:
            while val > k:
                val-=sequence[end]
                end+=1
        
        if val == k:
            arr.append([end,start-1])
    answer = arr[0]
    for val in arr[1:]:
        if answer[1]-answer[0]>val[1]-val[0]:
            answer=val
        elif answer[1]-answer[0]==val[1]-val[0] and answer[0]>val[0]:
            answer=val
    return answer