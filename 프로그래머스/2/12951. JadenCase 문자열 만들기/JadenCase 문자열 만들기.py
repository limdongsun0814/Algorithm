#122, 97
def solution(s):
    answer = ''
    flag = True
    for i in s:
        if flag:
            answer+=i.upper()
        else:
            answer+=i.lower()
        
        if i == " ":
            flag=True
        elif flag:
            flag=False
    return answer