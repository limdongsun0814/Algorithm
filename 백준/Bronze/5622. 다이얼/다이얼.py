A = input()
arr = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
sum = 0
for i in A:
    cnt=0
    for j in arr:
        for k in j:
            if k==i:
                sum+=cnt+3
        cnt+=1
print(sum)