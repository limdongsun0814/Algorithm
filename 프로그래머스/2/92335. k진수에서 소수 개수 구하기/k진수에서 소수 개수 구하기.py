def solution(n, k):
    answer = 0
    data = ""
    while n !=0:
        data=str(n%k)+data
        n=n//k
    arr = []
    value = ""
    for i in data:
        if i != "0":
            value+=i
        else:
            if value != "":
                arr.append(int(value))
                value=""
    if value !="":
        arr.append(int(value))
        
    checkArr = set(arr)
    findArr = []
    for i in checkArr:
        flag = True
        for j in range(2,int(i**0.5)+1):
            if i % j ==0:
                flag=False
                break
        if flag and i != 1:
            findArr.append(i)
    for i in arr:
        if i in findArr:
            answer+=1
    return answer