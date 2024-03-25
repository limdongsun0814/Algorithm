def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    n= len(citations)
    answer = 0
    cur = 0
    for i in range(len(citations)):
        h = n-i
        while cur <n and citations[cur]>=h:
            cur +=1

        if cur>=h and n-(cur)<=h:
            answer=h
            break
    return answer