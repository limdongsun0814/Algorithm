def back(value):
    global arr,w
    if 0<len(value)<=5:
        arr.append(value)
    if len(value)==5:
        return
    for i in w:
        back(value+i)

def solution(word):
    answer = 0
    global  arr,w
    w= ['A', 'E', 'I', 'O', 'U']
    arr = []
    back("")
    arr = list(set(arr))
    arr.sort()
    for i in range(len(arr)):
        if arr[i]==word:
            answer=i
            break
    return answer+1