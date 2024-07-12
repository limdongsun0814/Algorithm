def solution(s):
    answer = [0,0]
    while s != "1":
        cnt=cntZero(s)
        answer[1]+=cnt
        answer[0]+=1
        s=tranform(len(s)-cnt)
    return answer

def cntZero(s):
    result = 0
    for i in s:
        if i == "0":
            result+=1
    return result

def tranform(cnt):
    result = ""
    while cnt != 0:
        result= str(cnt%2)+result
        cnt=cnt//2
    return result