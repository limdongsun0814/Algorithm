def solution(rows, columns, queries):
    answer = []
    arr=[]
    for i in range(0,rows):
        flag=[]
        for j in range(1,columns+1):
            flag.append(i*columns+j)
        arr.append(flag)
    for que in queries:
        y1 = que[0]-1 # 1
        x1 = que[1]-1 # 1
        y2 = que[2]-1 # 4
        x2 = que[3]-1 # 3
        minValue = 100 * 100+1
        for x in range(x2,x1,-1):  
            flag = arr[y1][x]
            arr[y1][x]=arr[y1][x-1]
            arr[y1][x-1]=flag
            minValue = min(arr[y1][x],minValue)
        for y in range(y1,y2):
            flag = arr[y][x1]
            arr[y][x1]=arr[y+1][x1]
            arr[y+1][x1]=flag
            minValue = min(arr[y][x1],minValue)
        for x in range(x1,x2):
            flag = arr[y2][x]
            arr[y2][x]=arr[y2][x+1]
            arr[y2][x+1]=flag
            minValue = min(arr[y2][x],minValue)
        for y in range(y2,y1+1,-1):
            flag = arr[y][x2]
            arr[y][x2]=arr[y-1][x2]
            arr[y-1][x2]=flag
            minValue = min(arr[y][x2],minValue)
        minValue = min(flag,minValue)
        answer.append(minValue)
    return answer