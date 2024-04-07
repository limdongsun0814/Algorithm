def solution(stones, k):
    answer = 0
    left=0
    right=200000000
    while left<=right:
        cnt=0
        mid = (left+right)//2
        flag = True

        for i in stones:
            if i<=mid:
                cnt+=1
            else:
                cnt=0
            if cnt == k:
                flag=False
                break

        if flag:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    return answer