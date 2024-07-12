def solution(fees, records):
    answer = []
    start={}
    end={}
    price={}
    for data in records:
        t, number, check= data.split()
        if check=="IN":
            start[number]=tranform(t)
        else:
            if number not in end:
                end[number]=0
            end[number]+=tranform(t)-start[number]
            del start[number]
    for i in start:
        if i not in end:
            end[i]=0
        end[i]+=tranform("23:59")-start[i]
    key = list(end.keys())
    key.sort()
    for i in key:
        if max((end[i]-fees[0]),0)%fees[2]==0:
            answer.append(fees[1]+max((end[i]-fees[0]),0)*fees[3]//fees[2])
        else:
            answer.append(fees[1]+((end[i]-fees[0])//fees[2]+1)*fees[3])
            
    return answer

def tranform(t):
    arr=t.split(":")
    return int(arr[0])*60 + int(arr[1])