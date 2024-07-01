def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i,j in zip(name,yearning):
        dic[i]=j
    for i in photo:
        s=0
        for j in i:
            if j in dic:
                s+=dic[j]
        answer.append(s)
    return answer