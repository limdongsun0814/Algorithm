import collections
def solution(msg):
    answer = []
    key = {}
    for i in range(ord("A"),ord("Z")+1):
        key[chr(i)]=i-ord("A")+1
    
    msg = collections.deque(msg)
    data = ""
    while len(msg)>0:
        data+=msg.popleft()
        if data not in key:
            key[data]=len(key)+1
            answer.append(key[data[:-1]])
            data = data[-1]
    answer.append(key[data])
    return answer