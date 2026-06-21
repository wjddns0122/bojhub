def solution(n):
    '''
    피자를 나눠먹어야되는데 피자가 한판에 6조각. 피자가 한판에 6조각인데 한판을 무조건 다 먹어야됌
    그래서 n값이 4명 2판을 시켜야 12조각이 됌. 딱 맞아 떨어짐
    n값이 10명이면 5판을 시켜야 30조각이 됌
    n값이 3명이면? 한판이면 2조각
    n값이 2명이면? 한판이면 3조각
    6 = 1 x 2 x 3 x 6
    7명이면 42 최소 공배수
    8명이면 3판 24조각 6개
    '''
    answer = int(lcm(n, 6) // 6)
    return answer

def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)

print(solution(4))