def solution(land):
    maxValue=0
    dpM = land[0]
    for arr in land[1:]:
        # print(dpM)
        flag =[0,0,0,0]
        for i in range(4):
            copy=[j for j in dpM]
            del copy[i]
            flag[i]=max(copy)+arr[i]
        dpM=flag
    # print(dpM)
    
    return max(dpM)