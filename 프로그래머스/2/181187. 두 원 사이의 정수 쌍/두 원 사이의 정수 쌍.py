def solution(r1, r2):
    answer = 0
    for x in range(r2+1):
        if x <= r1:
            y1=(r1**2-x**2)**0.5
            y2=(r2**2-x**2)**0.5
            if y1 == int(y1):
                answer +=int(y2)-int(y1)+1
            else:
                answer +=int(y2)-int(y1)
        else:
            y2=(r2**2-x**2)**0.5
            answer+=int(y2)+1
            
    answer-=r2-r1+1
    return answer*4