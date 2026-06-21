def solution(numbers):
    arr = 0
    for i in range(len(numbers)):
        arr += numbers[i]
    answer = arr / len(numbers)
    return answer