def solution(my_strings, parts):
    answer = ''
    for i,j in zip(my_strings,parts):
        answer+=i[j[0]:j[1]+1]
    return answer