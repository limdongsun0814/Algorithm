def solution(phone_book):
    phone_book.sort()
    for index in range(len(phone_book)-1):
        answer = find(phone_book,index,phone_book[index])
        if answer:
            return False
    return True

def find(arr, index, val):
    if arr[index+1].startswith(arr[index]):
        return True
    return False