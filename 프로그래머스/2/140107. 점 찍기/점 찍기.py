def solution(k, d):
    answer = 0
    arr = [] # index => a
    for i in range(0,d+1,k):
        arr.append(0)
    for i in range(len(arr)):
        arr[i]=int(((d**2-(i*k)**2)**0.5)//k)+1
    # print(arr)
    return sum(arr)