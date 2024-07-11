def solution(want, number, discount):
    answer = 0
    dic = {}
    for i, j in zip(want,number):
        dic[i]=j
    
    dis = {}
    for i in discount[:10]:
        if i not in dis:
            dis[i]=0
        dis[i]+=1
    for i in range(len(discount)-10):
        if check(dic,dis):
            answer+=1
        dis[discount[i]]-=1
        if dis[discount[i]]==0:
            del dis[discount[i]]
        if discount[i+10] not in dis:
            dis[discount[i+10]]=0
        dis[discount[i+10]]+=1
    
    if check(dic,dis):
        answer+=1
    return answer

def check(dic,dis):
    flag = True
    for i in dic:
        if i in dis and dic[i] == dis[i]:
            pass
        else:
            flag=False
    return flag
