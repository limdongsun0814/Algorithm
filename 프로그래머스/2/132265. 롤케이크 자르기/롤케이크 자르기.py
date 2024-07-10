def solution(topping):
    answer = 0
    dic = {}
    keyCnt=0
    for i in topping:
        if i not in dic:
            dic[i]=0
            keyCnt+=1
        dic[i]+=1
    stack = set()
    for i in topping:
        stack.add(i);
        dic[i]-=1
        if dic[i]==0:
            keyCnt-=1
            del dic[i]
        if len(stack)==keyCnt:
            answer+=1
    
    return answer