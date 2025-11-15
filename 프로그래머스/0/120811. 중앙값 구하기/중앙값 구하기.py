def solution(array):
    array.sort()
    n = len(array)
    
    if n % 2 == 1:
        answer = array[n // 2]
    
    return answer