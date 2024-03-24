def solution(wallpaper):
    arr_x=[]
    arr_y=[]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                arr_x.append(i)
                arr_y.append(j)
    print(min(arr_x),min(arr_y),max(arr_x)+1,max(arr_y)+1)
    answer = [min(arr_x),min(arr_y),max(arr_x)+1,max(arr_y)+1]
    return answer