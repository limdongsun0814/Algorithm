n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr.sort()

nextValue = []
sumArr = []
for i in arr:
    nextValue.append(i)
    sumArr.append(sum(nextValue))
value=sum(nextValue)
if m-value>=0:
    print(max(nextValue))
else:
    cnt = n
    resultValue = 1
    while m-value<0:
        cnt-=1
        if cnt > 0:
            resultValue = arr[cnt - 1] + 1
            value = sumArr[cnt - 1] + resultValue * (n - cnt)
        else:
            resultValue =1
            value = resultValue * n
    print(resultValue+(m-value)//(n-cnt))