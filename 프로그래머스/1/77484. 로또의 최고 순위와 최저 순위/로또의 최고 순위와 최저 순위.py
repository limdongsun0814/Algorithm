def solution(lottos, win_nums):
    answer = []
    arr = set()
    cntZ = 0
    cnt = 0
    for i in lottos:
        if i==0:
            cntZ+=1
        elif i in win_nums:
            cnt+=1
        else:
            arr.add(i)
    print(arr, cntZ,cnt)
    
    if cnt+cntZ>=2:
        answer.append(7-(cnt+cntZ))
    else:
        answer.append(6)
    
    if cnt>=2:
        answer.append(7-cnt)
    else:
        answer.append(6)
        
    return answer