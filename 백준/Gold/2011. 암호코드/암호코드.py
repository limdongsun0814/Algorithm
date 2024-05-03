import sys
arr = list(map(int,list(input())))
n=len(arr)
dpM=[0]*(n+2)

if arr[0]==0:
    print(0)
    sys.exit()
else:
    dpM[0]=1

if n==1:
    print(1)
    sys.exit()

if arr[0]*10+arr[1]<=26 and arr[1]!=0:
    dpM[1]=2
elif  arr[0]*10+arr[1]<=26:
    dpM[1]=1
    dpM[0]=0
elif arr[0]*10+arr[1]>26 and arr[1]!=0:
    dpM[1]=1
else:
    print(0)
    sys.exit()

for i in range(2,n):
    flag=True
    if arr[i]!=0:# n-1
        dpM[i]+=dpM[i-1]
        flag=False
    if arr[i]+arr[i-1]*10 <=26 and arr[i]+arr[i-1]*10 !=0 and arr[i-1]!=0: #n-2
        dpM[i]+=dpM[i-2]
        flag=False
    if flag:
        print(0)
        sys.exit()
print(dpM[n-1]%1000000)