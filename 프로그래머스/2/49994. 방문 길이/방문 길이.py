def solution(dirs):
    move = {"U":[0,1],"D":[0,-1],"L":[-1,0],"R":[1,0]}
    pos = [0,0]
    arr = set()
    for i in dirs:
        nextValue = [pos[0]+move[i][0],pos[1]+move[i][1]]
        if -6<nextValue[0]<6 and -6<nextValue[1]<6:
            arr.add((pos[0],pos[1],nextValue[0],nextValue[1]))
            arr.add((nextValue[0],nextValue[1],pos[0],pos[1]))
            pos=nextValue
    print(arr)
    return int(len(arr)/2)