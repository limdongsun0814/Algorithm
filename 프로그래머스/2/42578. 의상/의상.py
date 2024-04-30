def solution(clothes):
    dic = {}
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]]=1
        dic[i[1]]+=1
    result = 1
    for i in dic:
        result*=dic[i]
    return result-1