import collections
import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    global answer
    answer = [[],[]]
    cnt=1
    for i in nodeinfo:
        i.append(cnt)
        cnt+=1
    nodeinfo.sort(key=lambda x:(-x[1],x[0]))
    nodeinfo=collections.deque(nodeinfo)
    value = nodeinfo.popleft()
    t = tree(value[2],value[0])
    while len(nodeinfo)>0:
        value = nodeinfo.popleft()
        t.insert(value[2],value[0])
    pre(t)
    post(t)
    return answer
def pre(t):
    global answer
    answer[0].append(t.node)
    if t.r != None:
        pre(t.r)
    if t.l != None:
        pre(t.l)
def post(t):
    global answer
    if t.r !=None:
        post(t.r)
    if t.l != None:
        post(t.l)
    answer[1].append(t.node)

class tree():
    def __init__(self,n,v):
        self.node=n
        self.value=v
        self.r=None
        self.l=None
    def getNode():
        return self.node
    
    def insert(self,n,v):
        if self.value>v:
            if self.r == None:
                self.r=tree(n,v)
            else:
                self.r.insert(n,v)
        else:
            if self.l == None:
                self.l=tree(n,v)
            else:
                self.l.insert(n,v)
                    