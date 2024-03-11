n = int(input())
k = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

# print(arr)
dic = {}

def dfs(useSet,cnt,val):
    if cnt == k:
        if dic.get(val,"not") == "not":
            dic[val] = 0
            return
        else:
            dic[val] += 1
            return

    for i in range(len(arr)):
        if i not in useSet:
            dfs(useSet+[i],cnt+1,val+str(arr[i]))

dfs([],0,"")

print(len(dic))
