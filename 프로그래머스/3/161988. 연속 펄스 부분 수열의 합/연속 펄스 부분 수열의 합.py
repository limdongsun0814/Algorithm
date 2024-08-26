import heapq
def solution(sequence):
    answer = 0
    dpM=[0]
    flag = 1
    for i in sequence:
        dpM.append(flag*i+dpM[-1])
        flag*=-1
    # print(dpM)
    minVal = []
    maxVal = []
    heapq.heappush(minVal,dpM[0]) # -100
    heapq.heappush(maxVal,-dpM[0]) # 100
    
    for i in dpM[1:]:
        if i >0 and answer < i-minVal[0] :
            answer = i-minVal[0]
        elif i<=0 and answer < -i-maxVal[0]:
            answer = -i-maxVal[0]
        heapq.heappush(minVal,i) # -100
        heapq.heappush(maxVal,-i) # 100
        
    return answer