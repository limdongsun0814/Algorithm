def solution(s):
    answer = []
    arr = {}
    for i in range(len(s)):
        if s[i] not in arr:
            answer.append(-1)
            arr[s[i]]=i+1
        else:
            answer.append(i+1-arr[s[i]])
            arr[s[i]]=i+1
            
    return answer