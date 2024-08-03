def solution(users, emoticons):
    global answer
    answer = [0,0]
    prices = []
    for em in emoticons:
        prices.append([int(em*0.9),int(em*0.8),(em//10)*7,int(em*0.6)])
    back(0,[],users,prices)
    return answer
def back(index,discounts,users,prices):
    if index == len(prices):
        global answer
        cnt,totalPrice=check(users,prices,discounts)
        if answer[0]<cnt:
            answer=[cnt,totalPrice]
        elif answer[0]==cnt and answer[1]<=totalPrice:
            answer=[cnt,totalPrice]
        else:
            pass
    else:
        discounts.append(0)
        back(index+1,discounts,users,prices)
        discounts.pop()
        
        discounts.append(1)
        back(index+1,discounts,users,prices)
        discounts.pop()
        
        discounts.append(2)
        back(index+1,discounts,users,prices)
        discounts.pop()
        
        discounts.append(3)
        back(index+1,discounts,users,prices)
        discounts.pop()
        
            
            


def check(users,prices,discounts):
    cnt = 0
    totalPrice=0
    for user in users:
        flagPrice = 0
        for price,discount in zip(prices,discounts):
            if user[0]<=(discount+1)*10:
                flagPrice+=price[discount]
        if flagPrice<user[1]:
            totalPrice+=flagPrice
        else:
            cnt+=1
    return cnt,totalPrice


