def solution(skill, skill_trees):
    answer = 0
    skillList = list(skill)
    for sk in skill_trees:
        cnt = 0
        flag=True
        for s in sk:
            if s in skillList:
                if s == skillList[cnt]:
                    cnt+=1
                else:
                    flag=False
                    break
        if flag:
            answer+=1
    return answer