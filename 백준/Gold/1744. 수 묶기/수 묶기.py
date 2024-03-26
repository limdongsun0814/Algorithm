N = int(input())
arr = []
arr2 = []
aaaa = []
zeroCnt = 0
for i in range(N):
    value = int(input())
    aaaa.append(value)
    if value==0:
        zeroCnt+=1
    if value>0:
        arr.append(value)
    elif value<0:
        arr2.append(value)
arr.sort(reverse=True)
arr2.sort()
aaaa.sort(reverse=True)
# print(arr)
if N == 1:
    print(aaaa[0])
else:
    sum = 0
    if len(arr)>0:
        number = len(arr)//2
        for i in range(number):
            if arr[i*2+1]==1 or arr[i*2]==1:
                sum+=arr[i*2]+arr[i*2+1]
            else:
                sum+=arr[i*2]*arr[i*2+1]
        if len(arr) %2 ==1:
            sum += arr[-1]

    if len(arr2)>0:
        check =True
        if zeroCnt ==0:
            number = len(arr2) // 2
        else:
            check=False
            number = len(arr2)//2
        if check:
            for i in range(number):
                sum += arr2[i * 2] * arr2[i * 2 + 1]
            if len(arr2) %2 ==1:
                sum += arr2[-1]
        else:
            for i in range(number):
                sum += arr2[i * 2] * arr2[i * 2 + 1]
    print(sum)