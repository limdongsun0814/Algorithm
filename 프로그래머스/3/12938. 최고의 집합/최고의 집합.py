def solution(n, s):
    answer = []
    if n>s:
        return [-1]
    for i in range(n):
        answer.append(s//n)
        if s%n!=0:
            answer[-1]+=1
            s-=1
    answer.sort()
    return answer