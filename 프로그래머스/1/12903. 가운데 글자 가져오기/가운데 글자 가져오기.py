def solution(s):
    answer = ''
    a = 0
    b = 0
    if len(s) % 2 == 1:
        a = len(s) // 2 
        answer = s[a]
    else:
        a = len(s) // 2 - 1
        b = len(s) // 2 
        answer = s[a] + s[b]
    return answer