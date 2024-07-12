def solution(n):
    answer = [] # (n+1)*n//2
    arr = []
    for i in range(1,n+1):
        arr.append([0]*i)
    start = [0,0]
    move = 0 # 0 아래 1 오른쪽 2 위
    
    for i in range(1,(n+1)*n//2+1):
        arr[start[0]][start[1]]=i
        if move == 0:
            if len(arr) == start[0]+1 or arr[start[0]+1][start[1]]!=0:
                move+=1
        elif move == 1:
            if len(arr[start[0]])==start[1]+1 or arr[start[0]][start[1]+1]!=0:
                move+=1
        else:
            if 0 == start[0] or arr[start[0]-1][start[1]-1]!=0:
                move=0
        
        if move == 0:
            start[0]+=1
        elif move == 1:
            start[1]+=1
        else:
            start[0]-=1
            start[1]-=1
            
    for i in arr:
        for j in i:
            answer.append(j)
            
    return answer