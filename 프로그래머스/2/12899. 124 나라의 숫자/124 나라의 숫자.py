def solution(n):
    result=tranform(n)
    return result

def tranform(n):
    result=""
    while n>0:
        if n%3==0:
            result="4"+result
            n=n//3-1
        else:
            result=str(n%3)+result
            n=n//3
    return result

    