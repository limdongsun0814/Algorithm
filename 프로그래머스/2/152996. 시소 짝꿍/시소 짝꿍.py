def solution(weights):
    answer = 0
    dic = {}
    for i in range(1000*2+1):
        dic[i]=0
        
    weights.sort()
    for i in weights:
        answer += dic[i]
        dic[i] += 1
        if i % 2 == 0:
            dic[(i//2) * 3] += 1
        if i % 3 == 0:
            dic[(i//3) * 4] += 1
        dic[i * 2] += 1
        
    return answer
