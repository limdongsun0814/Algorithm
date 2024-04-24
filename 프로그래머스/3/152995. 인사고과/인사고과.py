def solution(scores):
    answer = 1
    wanho = scores.pop(0)
    wanhoSum = sum(wanho)
    scores.sort(key=lambda x:(-x[0],x[1]))
    value=0
    for i in scores:
        if i[0]>wanho[0] and i[1]>wanho[1]:
            answer=-1
            break
        if value <= i[1]:
            value=i[1]
            if wanhoSum<sum(i):
                answer+=1

    return answer