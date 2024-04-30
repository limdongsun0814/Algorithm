def solution(progresses, speeds):
    answer = []
    day=0
    while len(speeds)>0:
        cnt=1
        prog = progresses.pop(0)
        speed = speeds.pop(0)
        day=(100-prog)//speed
        if (100-prog)%speed!=0:
            day+=1
        while len(progresses)>0:
            p,s = progresses.pop(0),speeds.pop(0)
            if p+s*day >=100:
                cnt+=1
            else:
                progresses.insert(0,p)
                speeds.insert(0,s)
                break
        answer.append(cnt)
    return answer