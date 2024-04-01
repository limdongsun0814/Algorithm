import sys

def dfp(value,target):
    global minValue,findValue
    # if value=="":
    #     newValue =abs(target)+len(value)+1
    # else:
    newValue =abs(target-int(value))+len(value)
    if newValue < minValue:
        minValue=newValue
        findValue = value

    if len(value)<len(str(target))+1:
        for i in arr2:
            dfp(value+i,target)



n = int(input())
M = int(input())
if M == 0:
    arr = []
else:
    arr = list(map(int,input().split()))

arr2 = []
for i in range(10):
    if i not in arr:
        arr2.append(str(i))
global minValue,findValue
minValue=sys.maxsize
findValue = ""
for i in arr2:
    dfp(i,n)
if findValue == "":
    findValue = "0"
if minValue<abs(n-100):
    print(minValue)
else:
    print(abs(n-100))


