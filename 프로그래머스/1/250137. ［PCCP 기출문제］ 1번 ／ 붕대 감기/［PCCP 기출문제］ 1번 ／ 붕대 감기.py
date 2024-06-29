def solution(bandage, health, attacks):
    t = 0
    conT = 0
    maxhealth=health
    attacks.reverse()
    while len(attacks)>0 and health > 0:
        t+=1
        if attacks[-1][0]==t:
            health-=attacks[-1][1]
            attacks.pop()
            conT=0
        else:
            health=min(maxhealth,health+bandage[1])
            conT+=1
            if conT==bandage[0]:
                conT=0
                health=min(maxhealth,health+bandage[2])
        # print(t,health)
    if health>0:
        answer=health
    else:
        answer=-1
    return answer