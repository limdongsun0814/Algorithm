import collections
import heapq
def solution(coin, cards):
    answer = 0
    stack=collections.deque(cards)
    n=len(cards)
    d = deq(n,coin)
    for i in range(n//3):
        value= stack.popleft()
        d.init_insert(value)
    # print(d)
    
    while True:
        answer+=1
        if len(stack)>1:
            val1 = stack.popleft()
            val2 = stack.popleft()
            d.insert(val1)
            d.insert(val2)
            # print(d)
            if len(d.stack) > 0:
                if d.pop():
                    break
                    
            else:
                break
        else:
            break
        
    
    return answer

class deq:
    def __init__(self,n,coin):
        self.dic={}
        self.stack=[]
        self.target=n+1
        self.g={}
        self.coin=coin
        
    def init_insert(self,value):
        s = abs(value-self.target)
        if s in self.dic:
            heapq.heappush(self.stack,[0,value,s])
            if self.dic[s]==1:
                del self.dic[s]
            else:
                self.dic[s]-=1
        elif value in self.dic:
            self.dic[value]+=1
        else:
            self.dic[value]=1
            
    def insert(self,value):
        s = abs(value-self.target)
        if s in self.dic :
            heapq.heappush(self.stack,[1,value,s])
            if self.dic[s]==1:
                del self.dic[s]
            else:
                self.dic[s]-=1
        
        elif s in self.g :
            heapq.heappush(self.stack,[2,value,s])
            if self.g[s]==1:
                del self.g[s]
            else:
                self.g[s]-=1
        
        elif value in self.dic:
            self.g[value]+=1
        else:
            self.g[value]=1
    
    def pop(self):
        if len(self.stack)<1:
            return True
        val=heapq.heappop(self.stack)
        self.coin -=val[0]
        return self.coin<0
            
    def __str__(self):
        return "dic: "+ str(self.dic) + " stack: "+ str(self.stack) + " target: "+ str(self.target) + " g: "+ str(self.g) + " coin: "+ str(self.coin)
        
        
        