import heapq

def solution(book_time):
    answer = 0
    arr = []
    for t in book_time:
        arr.append([int(t[0][:2])*60+int(t[0][3:]), int(t[1][:2])*60+int(t[1][3:])])
    arr.sort()
    stack = []
    for i in arr:
        while len(stack)>0:
            value=heapq.heappop(stack)
            if value+10 > i[0]:
                heapq.heappush(stack,value)
                break
                
        heapq.heappush(stack,i[1])
        answer=max(len(stack),answer)
    return answer