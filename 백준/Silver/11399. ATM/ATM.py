N = int(input())
arr = list(map(int,input().split()))
arr.sort()
arr2=[]
sumValue = 0
for i in arr:
    sumValue+=i
    arr2.append(sumValue)
print(sum(arr2))