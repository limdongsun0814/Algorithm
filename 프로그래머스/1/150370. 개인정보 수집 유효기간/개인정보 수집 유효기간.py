def solution(today, terms, privacies):
    answer = []
    today=tranform(today)
    termDict = {}
    for i in terms:
        data = i.split()
        termDict[data[0]]=int(data[1])
    for i in range(len(privacies)):
        data = privacies[i].split()
        data[0]=tranform(data[0])
        if today[1]<data[0][1]:
            data[0]=today[0]-data[0][0]-1
        else:
            data[0]=today[0]-data[0][0]
        if data[0]>=termDict[data[1]]:
            answer.append(i+1)
    return answer

def tranform(day):
    data = day.split(".")
    return [int(data[0])*12+int(data[1]),int(data[2])]