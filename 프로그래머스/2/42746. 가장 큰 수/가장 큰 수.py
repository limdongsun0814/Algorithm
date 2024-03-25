def solution(numbers):
    arr = []
    for i in numbers:
        arr.append(str(i))
    arr.sort(reverse=True,key=lambda x: x*4)
    answer = ''.join(arr)
    answer = str(int(answer))
    return answer