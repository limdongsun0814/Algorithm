def dp(mapArr,val):
    if len(val)==0:
        for i in mapArr:
            for j in i:
                print(j,end=" ")
            print()
        exit()

    value=val.pop(0)
    flagArr = set()
    x=3*(value[0]//3)
    y=3*(value[1]//3)
    for k in range(9):
        flagArr.add(mapArr[value[0]][k])
        flagArr.add(mapArr[k][value[1]])
        flagArr.add(mapArr[x+k//3][y+k%3])
    
    
    for i in range(1,10):
        if i not in flagArr:
            copyMap = [copy[:] for copy in mapArr]
            copyMap[value[0]][value[1]]=i
            dp(copyMap,val)
    val.insert(0,value)
            


arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))
# print(arr)

value = []

for i in range(9):
    for j in range(9):
        if arr[i][j]==0:
            value.append([i,j])

global result
result=[]
n=len(value)
dp(arr,value)