def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    arr = []
    for i in lost:
        for j in reserve:
            if i==j:
                arr.append(i)
    for i in arr:
        lost.remove(i)
        reserve.remove(i)
    for i in lost:
        flog = True
        for j in reserve:
            if j-1 == i or i == j+1:
                reserve.remove(j)
                flog=False
                break
        if flog:
            answer-=1
    return answer