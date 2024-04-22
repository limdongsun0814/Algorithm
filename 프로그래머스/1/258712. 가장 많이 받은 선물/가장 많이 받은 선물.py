def solution(friends, gifts):
    answer = 0
    preDic = {}
    cntDic = {}
    for i in friends:
        preDic[i]=0
        cntDic[i]=0

    dic = {}
    for i in gifts:
        data=i.split()
        if data[0] not in dic:
            dic[data[0]]=[]
        preDic[data[0]]+=1
        preDic[data[1]]-=1
        dic[data[0]].append(data[1])

    for i in range(len(friends)):
        for j in range(i,len(friends)):
            if friends[i] in dic:
                preCntA=dic[friends[i]].count(friends[j])
            else:
                preCntA=0

            if friends[j] in dic:
                preCntB=dic[friends[j]].count(friends[i])
            else:
                preCntB=0

            if preCntA > preCntB:
                cntDic[friends[i]]+=1
            elif preCntA < preCntB:
                cntDic[friends[j]]+=1
            else:
                pointA=preDic[friends[i]]
                pointB=preDic[friends[j]]
                if pointA>pointB:
                    cntDic[friends[i]]+=1
                elif pointA<pointB:
                    cntDic[friends[j]]+=1

    for i in cntDic:
        if answer < cntDic[i]:
            answer=cntDic[i]

    return answer