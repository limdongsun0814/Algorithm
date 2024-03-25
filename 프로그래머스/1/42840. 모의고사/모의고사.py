def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    if len(answers)>len(p1):
        p1*=int(len(answers)/len(p1))+1
    if len(answers)>len(p2):
        p2*=int(len(answers)/len(p2))+1
    if len(answers)>len(p3):
        p3*=int(len(answers)/len(p3))+1
    p1Cnt=0
    p2Cnt=0
    p3Cnt=0
    for i in range(len(answers)):
        if answers[i]==p1[i]:
            p1Cnt+=1
        if answers[i]==p2[i]:
            p2Cnt+=1
        if answers[i]==p3[i]:
            p3Cnt+=1
    maxValue = max(p1Cnt,p2Cnt,p3Cnt)
    answer = []
    if maxValue == p1Cnt:
        answer.append(1)
    if maxValue == p2Cnt:
        answer.append(2)
    if maxValue == p3Cnt:
        answer.append(3)
    return answer