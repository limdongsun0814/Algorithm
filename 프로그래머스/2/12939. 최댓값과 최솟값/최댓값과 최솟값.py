def solution(s):
    arr = list(map(int,s.split()))
    print(arr)
    
    return str(min(arr))+" "+str(max(arr))