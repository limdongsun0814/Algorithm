import copy
def solution(s):
    answer = []
    arr = []
    data= ""
    for i in s[1:-1]:
        if i == "{":
            flag=[]
        elif i=="}":
            arr.append(flag)
        elif i!=",":
            data+=i
        else:
            flag.append(int(data))
            data=""
        # print(flag,data,arr,i)
    flag.append(int(data))
    arr.append(flag)
    arr.sort(key=lambda x:len(x))
    # print(arr)
    dic = {}
    for i in arr:
        dicC = copy.deepcopy(dic)
        for j in i:
            if j not in dicC:
                if j in dic:
                    dic[j]+=1
                else:
                    dic[j]=1
                answer.append(j)
            else:
                dicC[j]-=1
                if dicC[j]==0:
                    del dicC[j]
    return answer