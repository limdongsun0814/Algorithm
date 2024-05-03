def solution(arr1, arr2):
    n1,m1 = len(arr1),len(arr1[0])
    m2,n2 = len(arr2[0]),len(arr2)
    answer = [[0 for i in range(m2)] for j in range(n1)]
    
    for i in range(n1):
        for j in range(m2):
            sumValue=0
            for k in range(m1):
                sumValue+=arr1[i][k]*arr2[k][j]
            answer[i][j]=sumValue
    return answer