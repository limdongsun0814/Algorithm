def solution(s):
    answer = False
    if len(s)==4 or len(s)==6:
        try:
            flag = int(s)
            answer=True
        except:
            pass
    return answer