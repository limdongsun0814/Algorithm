def p(start,to):
    result.append([start,to])
def move(index,start,to,vi):
    if index == 1:
        p(start,to)
    else:
        move(index-1,start,vi,to)
        p(start,to)
        move(index-1,vi,to,start)



n= int(input())
result  = []
move(n,1,3,2)
print(len(result))
for i in result:
    for j in i:
        print(j,end=" ")
    print()