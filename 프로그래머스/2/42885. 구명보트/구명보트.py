def solution(people, limit):
    answer = 0
    people.sort()
    cur = 0
    while len(people)-cur>1:
        if people[cur]+people[-1]<=limit:
            cur+=1
            people.pop()
        else:
            people.pop()
        answer+=1
    if len(people)-cur>0:
        answer+=1
    return answer