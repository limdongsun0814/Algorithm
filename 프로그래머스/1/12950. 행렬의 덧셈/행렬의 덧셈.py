import numpy
def solution(arr1, arr2):
    arr1 = numpy.array(arr1)
    arr2 = numpy.array(arr2)
    answer = (arr1+arr2).tolist()
    return answer