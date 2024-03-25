def solution(brown, yellow):
    answer = [0,0]
    for x in range(1,2500):
        if (brown+yellow)%x==0:
            y=(brown+yellow)/x
            if (x+y)*2-4==brown:
                answer[1] = int(x)
                answer[0] = int(y)
                break
    return answer