def solution(record):
    answer = []
    dic ={}
    keyWord = ['님이 들어왔습니다.','님이 나갔습니다.']
    result = []
    for data in record:
        arr=data.split()
        if arr[0] != "Leave":
            dic[arr[1]]=arr[2]
        else:
            result.append([True,arr[1]])
        if arr[0] == 'Enter':
            result.append([False,arr[1]])
    for i in result:
        if i[0]:
            answer.append(dic[i[1]]+keyWord[1])
        else:
            answer.append(dic[i[1]]+keyWord[0])
            
    return answer