def solution(prices):
    answer = [0]*len(prices)
    
    stack = []#값 index
    for i in range(len(prices)):
        for j in stack:
            answer[j[1]]+=1
        while len(stack)>0 and stack[-1][0]>prices[i]:
            stack.pop()
        stack.append([prices[i],i])
    
    return answer