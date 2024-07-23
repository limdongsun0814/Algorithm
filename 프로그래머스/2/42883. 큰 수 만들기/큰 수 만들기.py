def solution(number, k):
    answer = ''
    stack = [0]
    k+=1
    target=len(number)-k
    for i in list(map(int, number)):
        while len(stack)>0 and stack[-1] < i and k!=0:
            stack.pop()
            k-=1
        stack.append(i)
    for i in stack:
        answer+=str(i)
    return answer[:target+1]