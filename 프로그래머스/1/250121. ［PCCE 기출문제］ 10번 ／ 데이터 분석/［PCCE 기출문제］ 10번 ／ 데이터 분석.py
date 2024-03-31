def solution(data, ext, val_ext, sort_by):
    cheak =[]
    if ext == "date":
        yearExt = int(str(val_ext)[:4])
        mExt = int(str(val_ext)[4:6])
        dExt = int(str(val_ext)[6:8])
        print(yearExt,mExt,dExt)

        for i in data:
            year = int(str(i[1])[:4])
            m = int(str(i[1])[4:6])
            d = int(str(i[1])[6:8])
            if year < yearExt:
                cheak.append(i)
            elif year == yearExt and m < mExt:
                cheak.append(i)
            elif year == yearExt and m == mExt and d < dExt:
                cheak.append(i)
    elif ext == "code":
        for i in data:
            code = i[0]
            if code < val_ext:
                cheak.append(i)
    elif ext == "maximum":
        for i in data:
            maximum = i[2]
            if maximum < val_ext:
                cheak.append(i)
    elif ext == "remain":
        for i in data:
            remain = i[3]
            if remain < val_ext:
                cheak.append(i)

    if sort_by=="code":
        cheak.sort(key=lambda x:x[0])
    elif sort_by=="date":
        cheak.sort(key=lambda x:x[1])
    elif sort_by=="maximum":
        cheak.sort(key=lambda x:x[2])
    elif sort_by=="remain":
        cheak.sort(key=lambda x:x[3])
    answer = cheak
    return answer