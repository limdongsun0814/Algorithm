def solution(numbers):
    answer = []
    
    
    for number in numbers:
        if number <= 1:
            answer.append(number)
            continue
        target = bin(number)[2:]
        n=len(target)
        value=3
        while value<n:
            value=2*value+1
        
        target = (value-len(target))*"0" + target
        flag=dfs(target)
        if flag:
            answer.append(0)
        else:
            answer.append(1)
    print(answer)
    return answer

def dfs(value):
    n=len(value)
    if n>=1:
        if value[n//2]=="0":
            if "0"*n!=value:
                return True
        else:
            left=value[:n//2]
            right=value[n//2+1:]
            flag = dfs(left)
            if flag:
                return True
            flag = dfs(right)
            if flag:
                return True
    
    
    
    
    
    