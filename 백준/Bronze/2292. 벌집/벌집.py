A = int(input())

n = 6
sum = 2
cnt =1
if A==1:
    print('1')
elif A<=7:
    print('2')
else:
    while A>=sum:
        cnt+=1
        sum += n 
        n+=6
    print(cnt)