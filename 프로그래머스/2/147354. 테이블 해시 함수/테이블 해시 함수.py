def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x:(x[col-1],-x[0]))
    arr = []
    # print(data)
    for i in range(row_begin,row_end+1):
        value = 0
        for j in data[i-1]:
            value+=j%i
        arr.append(value)
    # print(arr)
    value = 0
    for i in arr:
        value = i ^ value
    return value