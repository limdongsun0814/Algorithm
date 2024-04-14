import heapq

def solution(plans):
    arr = []
    for i in plans:
        h,m = map(int,i[1].split(":"))
        arr.append([h*60+m,i[0],int(i[2])])
    # arr.sort(key=lambda x:x[1])
    heapq.heapify(arr)
    using = []
    size = len(arr)
    answer = []
    flag=True
    while len(answer)!=size and len(arr) >0:
        value = heapq.heappop(arr)
        if len(arr)>0:
            value2=heapq.heappop(arr)
        else:
            flag = False
            answer.append(value[1])
            break

        if value[0]+value[2] == value2[0]:
            answer.append(value[1])
            heapq.heappush(arr,value2)
        elif value[0]+value[2] > value2[0]:
            using.append([value[1],value[2]-(value2[0]-value[0])]) # 종류 , 남은시간
            heapq.heappush(arr,value2)
        else:
            answer.append(value[1])
            t = value2[0]-(value[0]+value[2])
            while len(using)>0 and t>0:
                    value3 = using.pop()
                    t-=value3[1]
                    if t >=0:
                        answer.append(value3[0])
                    else:
                        using.append([value3[0],-t])
            heapq.heappush(arr,value2)

    if flag:
        answer.append(value2[1])
    using.reverse()
    for i in using:
        answer.append(i[0])
    return answer