import collections
import copy
def solution(expression):
    global answer
    answer = []
    arr = collections.deque()
    arr.append(0)
    for i in expression:
        if i in ("-","*","+"):
            arr.append(i)
            arr.append(0)
        else:
            arr[-1]=int(str(arr[-1])+i)
    # print(arr)
    
    dfs(arr,[False,False,False],0)
    
    return max(answer)

def sumFunction(arr,fu):
    result=collections.deque()
    arr2 = copy.deepcopy(arr)
    while len(arr2)>0:
        value = arr2.popleft()
        if value == fu:
            if fu == "+":
                result[-1]+=int(arr2.popleft())
            elif fu == "-":
                result[-1]-=int(arr2.popleft())
            else:
                result[-1]*=int(arr2.popleft())
                
        else:
            result.append(value)
    return result

def dfs(arr, visit,index):
    if False not in visit:
        global answer
        answer.append(abs(arr[0]))
    else:
        if visit[0]==False:
            visit[0]=True
            dfs(sumFunction(arr,"+"),visit,index+1)
            visit[0]=False
        
        if visit[1]==False:
            visit[1]=True
            dfs(sumFunction(arr,"-"),visit,index+1)
            visit[1]=False
        
        
        if visit[2]==False:
            visit[2]=True
            dfs(sumFunction(arr,"*"),visit,index+1)
            visit[2]=False