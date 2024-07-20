def solution(n):
    global answer
    answer = 0
    back(0,[],n)
    return answer

def back(index,stack,n):
    if index==n:
        global answer
        answer+=1
    else:
        for i in range(n):
            if i not in stack:
                flag = True
                for j in range(index):
                    if index-i == j-stack[j] or n+1-index-i==n+1-j-stack[j]:
                        flag=False
                        break
                if flag:
                    stack.append(i)
                    back(index+1,stack,n)
                    stack.pop()
                    
                    
                    
                    