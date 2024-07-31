import collections
def solution(m, musicinfos):
    answer = '(None)'
    argmax = 0
    m=collections.deque(m)
    
    arr = []
    for i in m:
        if i != "#":
            arr.append(i)
        else:
            arr[-1]+="#"
    m=collections.deque(arr)
    
    for music in musicinfos:
        t,name,mu=tranform(music)
        if len(mu)>=len(m):
            stack = collections.deque()
            for i in m:
                stack.append(mu.popleft())
            while len(mu)>0:
                if stack == m:
                    if argmax < t:
                        answer=name
                        argmax=t
                    break
                else:
                    stack.popleft()
                    stack.append(mu.popleft())
            if stack == m:
                if argmax < t:
                    answer=name
                    argmax=t
    return answer

def tranform(music):
    data = music.split(",")
    t = int(data[1][:2])*60+int(data[1][3:])-(int(data[0][:2])*60+int(data[0][3:]))+1
    name = data[2]
    arr = []
    for i in data[3]:
        if i != "#":
            arr.append(i)
        else:
            arr[-1]+="#"
    result=arr*(t//len(arr))+arr[:t%len(arr)]
    result=collections.deque(result)
    return t,name,result