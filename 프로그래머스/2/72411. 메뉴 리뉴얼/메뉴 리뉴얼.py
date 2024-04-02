def dfs(value,index,n,target):
    global arr
    if len(value)==n:
        arr.append(value)
        return
    if index >= len(target):
        return
    dfs(value+target[index],index+1,n,target)
    dfs(value,index+1,n,target)

def solution(orders, course):
    answer = []

    # for i in course:
    for j in range(len(orders)):
        for k in range(j+1,len(orders)):
            flog = ""
            for x in orders[k]:
                if x in orders[j]:
                    flog+=x
            if flog !="":
                arr99 = []
                for x in flog:
                    arr99.append(x)
                arr99.sort()
                flog =""
                for x in arr99:
                    flog+=x
                answer.append(flog)
    # print(answer)
    result = []
    for n in course:
        global arr
        arr =[]
        for i in answer:
            dfs("",0,n,i)
        # print(arr)
        maxValue = ""
        argmax = 0
        for i in arr:
            cnt = arr.count(i)
            if cnt > argmax:
                maxValue=[i]
                argmax=cnt
            elif cnt == argmax:
                maxValue.append(i)
        for i in list(set(maxValue)):
            result.append(i)
    result.sort()
    return result