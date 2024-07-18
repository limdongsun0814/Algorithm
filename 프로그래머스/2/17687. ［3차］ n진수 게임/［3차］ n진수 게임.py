
number = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
def solution(n, t, m, p):
    answer = ''
    start = 0
    cnt=1
    if m == p:
        p=0
    while len(answer)<=t:
        value = tranform(start,n)
        for i in value:
            if cnt % m==p:
                answer+=i
            cnt+=1
        start+=1
    
    return answer[:t]

def tranform(num,n):
    result = ''
    while num>=n:
        result = number[num%n]+result
        num= num//n
    return number[num]+result