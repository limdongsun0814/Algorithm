import heapq
def solution(operations):
    answer = []
    maxheapq = []
    
    minheapq = []
    for i in operations:
        data = i.split()
        if data[0]=="I":
            heapq.heappush(maxheapq,-int(data[1]))
            heapq.heappush(minheapq,int(data[1]))
        else:
            if len(minheapq)>0:
                if data[1]=="1":
                    minheapq.remove(-heapq.heappop(maxheapq))
                else:
                    maxheapq.remove(-heapq.heappop(minheapq))
    print(maxheapq,minheapq)
    if maxheapq==[]:
        return [0,0]
        
    return [-maxheapq[0],minheapq[0]]