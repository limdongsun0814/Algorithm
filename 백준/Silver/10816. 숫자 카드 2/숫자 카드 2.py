input()
dic = {}
for i in input().split():
    if i not in dic:
        dic[i]=0
    dic[i]+=1

input()

for i in input().split():
    if i in dic:
        print(dic[i],end=" ")
    else:
        print(0, end=" ")