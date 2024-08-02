def solution(s):
    answer = True
    r=0
    l=0
    check=True
    for i in s:
        if i == "(":
            r+=1
        else:
            l+=1
        
        if r<l:
            check=False
            break
    check= check and r==l

    return check