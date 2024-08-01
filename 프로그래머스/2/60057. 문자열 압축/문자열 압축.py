def solution(s):
    answer = len(s)+1
    for i in range(1,len(s)+1):
        data=tranfrom(s,i)
        cnt=len(data)
        if cnt<answer:
            answer=cnt
    return answer

def tranfrom(s,n):
    result=""
    stack = s[:n]
    index = n
    cnt=1
    while index<len(s):
        newValue = s[index:index+n]
        if stack == newValue:
            cnt+=1
        else:
            if cnt != 1:
                result+=str(cnt)+stack
            else:
                result+=stack
                
            stack=newValue
            cnt=1
        index+=n
    if cnt != 1:
        result+=str(cnt)+stack
    else:
        result+=stack
    return result