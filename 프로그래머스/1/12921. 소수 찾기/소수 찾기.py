def solution(n):
    answer = set()
    answer.add(1)
    for i in range(2,n+1):
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                answer.add(i)
                break
    return n-len(answer)