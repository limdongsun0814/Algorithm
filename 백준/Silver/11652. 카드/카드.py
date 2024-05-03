n = int(input())
dic = {}
for i in range(n):
    m = int(input())
    if m not in dic:
        dic[m]=0
    dic[m]+=1

argMax=0
maxValue=-2**63-1
for i in dic:
    if dic[i] > maxValue:
        maxValue=dic[i]
        argMax=i
    elif dic[i] == maxValue and i < argMax:
        argMax=i
print(argMax)