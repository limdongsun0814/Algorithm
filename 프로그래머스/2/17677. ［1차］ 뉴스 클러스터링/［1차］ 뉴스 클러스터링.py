import collections
def solution(str1, str2):
    answer = 0
    total = 0
    str1=str1.lower()
    str2=str2.lower()
    strList1 = []
    strList2 = []
    for i,j in zip(str1,str1[1:]):
        if ord("a")<=ord(i)<=ord("z") and ord("a")<=ord(j)<=ord("z"):
            strList1.append(i+j)
    for i,j in zip(str2,str2[1:]):
        if ord("a")<=ord(i)<=ord("z") and ord("a")<=ord(j)<=ord("z"):
            strList2.append(i+j)
    
    strDict1 = {}
    for i in strList1:
        if i not in strDict1:
            strDict1[i]=0
        strDict1[i]+=1
    
    for i in strList2:
        if i in strDict1:
            total+=1
            answer+=1
            strDict1[i]-=1
            if strDict1[i]==0:
                del strDict1[i]
        else:
            total+=1
            
    for i in strDict1:
        total+=strDict1[i]
    if answer==total:
        return 65536
    return int(answer*65536/total)