import sys
sys.setrecursionlimit(10**5)
class Node():
    def __init__(self,node):
        self.node = node
        self.right=None
        self.left=None
    def insert(self,value):
        if self.node > value:
            if self.left is None:
                self.left=Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right=Node(value)
            else:
                self.right.insert(value)

def dfs(node):
    if node.left is not None:
        dfs(node.left)
    if node.right is not None:
        dfs(node.right)
    result.append(node.node)

arr = []
try:
    while True:
        arr.append(int(input()))
except:
    pass
n = Node(arr[0])

for i in arr[1:]:
    n.insert(i)

result = []
dfs(n)
result = list(set(result))

for i in result:
    print(i)