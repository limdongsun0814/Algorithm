import collections
def solution(n, words):
    answer = [0,0]
    using = set()
    size=0
    words.reverse()
    
    valOld=words.pop()
    using.add(valOld)
    size+=1
    while len(words)>0:
        value = words.pop()
        if value[0]!=valOld[-1]:
            answer=[len(using)%n+1,len(using)//n+1]
            break
        else:
            using.add(value)
            size+=1
            if size!=len(using):
                answer=[len(using)%n+1,len(using)//n+1]
                break
            
        valOld=value
    return answer