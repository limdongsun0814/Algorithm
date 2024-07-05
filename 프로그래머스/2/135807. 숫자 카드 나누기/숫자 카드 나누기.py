def solution(arrayA, arrayB):
    answer = [0]
    minA = min(arrayA)
    for i in range(1,int(minA**0.5)+1):
        if minA%i==0:
            A,B = minA//i,i
            check(A,answer,arrayA,arrayB)
            check(B,answer,arrayA,arrayB)
    # print(answer)
    # answer = [0]
    minA = min(arrayB)
    for i in range(1,int(minA**0.5)+1):
        if minA%i==0:
            A,B = minA//i,i
            check(A,answer,arrayB,arrayA)
            check(B,answer,arrayB,arrayA)
    return max(answer) 
def check(A,answer,arrayA,arrayB):
    flag = True
    # print(A,1)
    for j in arrayA:
        if j % A !=0:
            flag=False
            # print(j,A,arrayA,1000)
            break
    if flag:
        for j in arrayB:
            if j % A ==0:
                flag=False
                break
        if flag:
            answer.append(A)