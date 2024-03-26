data = input()
arr = []
strValue = ""
for i in data:
    if i != "-" and i != "+":
        strValue+=i
    else:
        arr.append(int(strValue))
        strValue=i
arr.append(int(strValue))
flog = True
arr2 = []
flogArr = []
for i in arr:
    if i<0:
        flog=not flog
        arr2.append(sum(flogArr))
        flogArr=[]
    flogArr.append(abs(i))
arr2.append(sum(flogArr))
sumValue  = arr2[0]
for i in arr2[1 :]:
    sumValue-=i
print(sumValue)