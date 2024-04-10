import copy
def makeG():
    dic ={}
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]]=[]
        dic[arr[i]].append(i+1)
    return dic
n = int(input())
arr= []
for i in range(n):
    arr.append(int(input()))

dic=makeG()

result = []

visit = {}
for i in dic:
    visit[i]=False

for i in dic:
    copyVisit=copy.deepcopy(visit)
    copyVisit[i]=True
    stack=[i]
    while len(stack)>0:
        value=stack.pop(0)
        for j in dic[value]:
            if j in copyVisit and copyVisit[j]==False:
                copyVisit[j]=True
                stack.append(j)
            elif j in copyVisit and copyVisit[j]==True:
                result.append(i)
                break
result.sort()
print(len(result))
for i in result:
    print(i)