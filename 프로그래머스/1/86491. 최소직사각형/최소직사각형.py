def solution(sizes):
    arrX=[]
    arrY=[]
    for i in sizes:
        if i[0]>i[1]:
            arrX.append(i[0])
            arrY.append(i[1])
        else:         
            arrX.append(i[1])
            arrY.append(i[0])
    return max(arrX)*max(arrY)