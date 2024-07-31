def solution(p):
    if p=="":
        return ""
    answer = dfs(p)
    
    return answer

def dfs(data):
    if data == "":
        return ""
    u,v=tranfrom(data)
    if check(u):
        return u+dfs(v)
    else:
        flag = "("
        flag+=dfs(v)
        flag+=")"
        for i in u[1:-1]:
            if i == ")":
                flag+="("
            elif i=="(":
                flag+=")"
        return flag
def check(data):
    r,l = 0,0
    for i in data:
        if i == "(":
            r+=1
        elif i == ")":
            l+=1
        if r<l:
            return False
    return True

def tranfrom(data):
    u,v = "",""
    r,l=0,0
    case = False
    for i in data:
        if i == "(":
            r+=1
        elif i == ")":
            l+=1
        if case==False:
            u+=i
        else:
            v+=i
        if r==l:
            case=True
    return u,v