def solution(n):
    answer = ''
    i = 0
    while True:
        i += 1
        if i % 2 == 1:
            answer += '수'
        elif i % 2 == 0:
            answer += '박'
        
        if i == n:
            break
    return answer

print(solution(3))