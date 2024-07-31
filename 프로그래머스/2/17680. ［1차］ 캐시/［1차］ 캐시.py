import collections
def solution(cacheSize, cities):
    answer = 0
    key = set()
    stack = collections.deque()
    for city in cities:
        city=city.lower()
        if city in key:
            stack.remove(city)
            stack.append(city)
            answer+=1
        else:
            answer+=5
            key.add(city)
            stack.append(city)
            if len(key)>cacheSize:
                key.remove(stack.popleft())
    return answer