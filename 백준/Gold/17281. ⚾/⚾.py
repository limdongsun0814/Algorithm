from itertools import permutations

arr = [1,2,3,4,5,6,7,8]
arr2 = []
n = int(input())
for i in range(n):
    arr2.append(list(map(int,input().split())))

ans =0
for i in permutations(arr,8):
    a = list(i)
    i=a[:3]+[0]+a[3:]
    ansCnt = 0
    for j in range(n):
        outCnt = 0 
        # mapArr = [0]*3
        p1,p2,p3=0,0,0
        while outCnt<3:
            value=i.pop(0)
            if arr2[j][value]==0:
                outCnt+=1
            elif arr2[j][value]==1:
                # ansCnt+=mapArr[2]
                # mapArr = [1,mapArr[0],mapArr[1]]
                ansCnt+=p3
                p3 = p2
                p2 = p1
                p1 = 1
            elif arr2[j][value]==2:
                # ansCnt+=mapArr[2]+mapArr[1]
                # mapArr = [0,1,mapArr[0]]
                ansCnt+=p3+p2
                p3 = p1
                p2 = 1
                p1 = 0
            elif arr2[j][value]==3:
                # ansCnt+=mapArr[2]+mapArr[1]+mapArr[0]
                # mapArr = [0,0,1]
                ansCnt+=p3+p2+p1
                p3 = 1
                p2 = 0
                p1 = 0
            else:
                # ansCnt+=mapArr[2]+mapArr[1]+mapArr[0]+1
                # mapArr = [0,0,0]
                ansCnt+=p3+p2+p1+1
                p3 = 0
                p2 = 0
                p1 = 0
            i.append(value)
    ans = max(ans,ansCnt)
print(ans)