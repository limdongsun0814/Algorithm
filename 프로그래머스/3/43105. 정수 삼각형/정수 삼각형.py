def solution(triangle):
    dpM=[]
    dpM.append([0,triangle[0][0],0])
    for i in range(len(triangle)-1):
        flag=[0]
        for j in range(len(triangle[i+1])):
            flag.append(max(dpM[i][j],dpM[i][j+1])+triangle[i+1][j])
        flag.append(0)
        dpM.append(flag)
    return max(dpM[-1])