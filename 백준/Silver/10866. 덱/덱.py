import sys

from collections import deque

d = deque()

n = int(input())
cnt=0
for i in range(n):
    check = sys.stdin.readline().rstrip().split()
    if check[0]=="push_back":
        value=check[1]
        cnt+=1
        d.append(value)
    elif check[0]=="push_front":
        value=check[1]
        cnt+=1
        d.appendleft(value)
    elif check[0]=="pop_front":
        if cnt>0:
            value = d.popleft()
            cnt-=1
        else:
            value=-1
        print(value)
    elif check[0]=="pop_back":
        if cnt>0:
            value = d.pop()
            cnt-=1
        else:
            value=-1
        print(value)
    elif check[0]=="size":
        print(cnt)
    elif check[0]=="empty":
        if cnt>0:
            print(0)
        else:
            print(1)
    elif check[0]=="front":
        if cnt>0:
            value=d.popleft()
            d.appendleft(value)
        else:
            value=-1
        print(value)
    elif check[0]=="back":
        if cnt>0:
            value=d.pop()
            d.append(value)
        else:
            value=-1
        print(value)
        