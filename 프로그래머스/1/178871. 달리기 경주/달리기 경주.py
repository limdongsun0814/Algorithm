def solution(players, callings):
    answer = []
    dic = {}
    for i in range(len(players)):
        dic[players[i]]=i
    for i in callings:
        flag = dic[i]
        dic[players[flag-1]]+=1
        dic[i]-=1
        players[dic[players[flag-1]]]=players[flag-1]
        players[dic[i]]=i
    return players