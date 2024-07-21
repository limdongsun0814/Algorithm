import collections
def solution(keymap, targets):
    answer = []
    keyDict = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in keyDict:
                keyDict[key[i]]=i+1
            else:
                keyDict[key[i]]=min(keyDict[key[i]],i+1)
    for target in targets:
        value = 0
        for t in target:
            if t not in keyDict:
                value = -1
                break
            else:
                value+=keyDict[t]
        answer.append(value)
    return answer