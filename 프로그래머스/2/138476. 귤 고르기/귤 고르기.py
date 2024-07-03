def solution(k, tangerine):
    answer = 0
    dic={}
    for i in tangerine:
        if i not in dic:
            dic[i]=0
        dic[i]+=1
        
    arr = []
    for key in dic:
        arr.append([key,dic[key]])
    arr.sort(key=lambda x:(-x[1]),reverse=True )
    
    box = 0
    while len(arr)>0:
        value=arr.pop()
        if box+value[1]<=k:
            box+=value[1]
            answer+=1
        else:
            answer+=1
            break
        if box==k:
            break
    return answer