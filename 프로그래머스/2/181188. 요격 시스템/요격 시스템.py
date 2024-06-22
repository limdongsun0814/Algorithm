def solution(targets):
    answer = 0
    targets.sort()
    m = 0
    for target in targets:
        if m > target[0]: # 그안에 종속되어 있으면 
            m=min(target[1],m)
        else:
            m=target[1]
            answer+=1
    return answer