def solution(numbers):
    answer = []
    stack = []
    numbers.reverse()
    for i in range(len(numbers)):
        flag=True
        while len(stack) >0:
            if stack[-1]>numbers[i]:
                answer.append(stack[-1])
                flag=False
                break
            else:
                stack.pop()
        if flag:
            answer.append(-1)
        stack.append(numbers[i])
        
    answer.reverse()
    return answer