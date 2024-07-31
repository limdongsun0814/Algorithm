import collections
def solution(files):
    answer = []
    arr = []
    for file in files:
        head, number, tail = tranfrom(file)
        arr.append([head,number,tail])
    arr.sort(key=lambda x:(x[0].upper(),int(x[1])))
    for i in arr:
        answer.append(i[0]+i[1]+i[2])
    return answer

def tranfrom(data):
    head = ""
    number=""
    tail= ""
    case = 0
    
    data = collections.deque(list(data))
    while len(data)>0:
        value = data.popleft()
        if case == 0 and ( ord("0")>ord(value) or ord("9")<ord(value) ):
            head+=value
        elif case == 0 and ( ord("0")<=ord(value) and ord("9")>=ord(value) ):
            case+=1
            number+=value
        elif case == 1 and ( ord("0")<=ord(value) and ord("9")>=ord(value) ):
            number+=value
        elif case == 1 and ( ord("0")>ord(value) or ord("9")<ord(value) ):
            case+=1
            tail+=value
        else:
            tail+=value
    return head, number, tail