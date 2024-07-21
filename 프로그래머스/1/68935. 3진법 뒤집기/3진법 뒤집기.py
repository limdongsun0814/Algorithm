def solution(n):
    answer=0
    flag=tranform(n)
    cnt = 0
    for i in flag:
        answer+=int(i)*3**cnt
        cnt+=1
    return answer

def tranform(n):
    result = ""
    while n>2:
        result = str(n % 3) + result
        n=n//3
        
    return str(n)+result