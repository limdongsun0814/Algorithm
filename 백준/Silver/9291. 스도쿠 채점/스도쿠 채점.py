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

            

n = int(input())
for _ in range(n):
    arr = []
    for i in range(9):
        arr.append(list(map(int, input().split())))
    
    try:
        input()
    except:
        pass

    if checkF(arr):
        print("Case %d: CORRECT" %(_+1))
    else:
        print("Case %d: INCORRECT" %(_+1))