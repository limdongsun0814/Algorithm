def f1(value):
    print(value,end="")
    for i in dic[value]:
        if i != ".":
            f1(i)
def f2(value):
    if dic[value][0]!=".":
        f2(dic[value][0])
    print(value,end="")
    if dic[value][1]!=".":
        f2(dic[value][1])
def f3(value):
    if dic[value][0]!=".":
        f3(dic[value][0])
    if dic[value][1]!=".":
        f3(dic[value][1])
    print(value,end="")

n = int(input())
dic = {}
for i in range(n):
    arr = input().split()
    dic[arr[0]]=[arr[1],arr[2]]

f1("A")
print()
f2("A")
print()
f3("A")