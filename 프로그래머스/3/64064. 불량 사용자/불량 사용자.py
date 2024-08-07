import collections
def solution(user_id, banned_id):
    global answer
    answer = set()
    user_id=collections.deque(user_id)
    banned_id=collections.deque(banned_id)
    dfs(user_id,banned_id,[],0)
    return len(answer)
def dfs(user_id,banned_id,value,index):
    if len(banned_id)==index:
        global answer
        copyValue = value[:]
        copyValue.sort()
        answer.add(tuple(copyValue))
    else:
        n=len(user_id)
        banned=banned_id[index]
        for i in range(n):
            user = user_id.popleft()
            if check(user,banned):
                value.append(user)
                dfs(user_id,banned_id,value,index+1)
                value.pop()
            user_id.append(user)
                


def check(user,banned):
    for i,j in zip(user,banned):
        if j != "*" and i != j:
            return False
    return len(user)==len(banned)