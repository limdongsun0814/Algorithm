def checkF(mapArr):
    flag = True
    
    for i in range(9):
        for j in range(9):
            x=3*(i//3)
            y=3*(j//3)
            flag1 = []
            flag2 = []
            flag3 = []

            for k in range(9):
                if mapArr[i][k] not in flag1 or mapArr[i][k]==0:
                    flag1.append(mapArr[i][k])
                else:
                    return False
                
                if mapArr[k][j] not in flag2 or mapArr[k][j]==0:
                    flag2.append(mapArr[k][j])
                else:
                    return False
                
                if mapArr[x+k//3][y+k%3] not in flag3 or mapArr[x+k//3][y+k%3]==0:
                    flag3.append(mapArr[x+k//3][y+k%3])
                else:
                    return False
    return flag


def dp(mapArr,val):
    if len(val)==0:
        for i in mapArr:
            for j in i:
                print(j,end="")
            print()
        print()
        return True
    
    value=val.pop(0)
    flagArr = set()
    x=3*(value[0]//3)
    y=3*(value[1]//3)
    for k in range(9):
        flagArr.add(mapArr[value[0]][k])
        flagArr.add(mapArr[k][value[1]])
        flagArr.add(mapArr[x+k//3][y+k%3])
    
    
    check = False
    for i in range(1,10):
        if i not in flagArr:
            copyMap = [copy[:] for copy in mapArr]
            copyMap[value[0]][value[1]]=i
            check=dp(copyMap,val)
            if check:
                return check
    val.insert(0,value)
            

n = int(input())
for _ in range(n):
    arr = []
    for i in range(9):
        arr.append(list(map(int, list(input()))))

    if checkF(arr):
        value = []
        for i in range(9):
            for j in range(9):
                if arr[i][j]==0:
                    value.append([i,j])
        
        check=dp(arr,value)
        if check==None:
            print("Could not complete this grid.")
            print()
    else:
        print("Could not complete this grid.")
        print()