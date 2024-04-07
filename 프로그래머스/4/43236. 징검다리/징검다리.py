def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    arr = []
    end =0
    for i in rocks:
        arr.append(i-end)
        end=i
    left = 0
    right = 1000000000
    result=0
    while left<right:
        mid = (left+right)//2
        cnt = 0
        dis = 0
        for i in arr:
            dis+=i
            if dis<mid:
                cnt+=1
            else:
                dis=0

        if cnt<n:
            left=mid+1
        elif cnt>n:
            right=mid
        else:
            left=mid+1
            

    return left-1