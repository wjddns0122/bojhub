import math

# 입력 받기
a, b, v = map(int, input().split())

# 목표 높이를 초과하기 위해 필요한 일수 계산
# 마지막 날에 아침에 자르고 목표 높이에 도달하면 하루가 추가되지 않음
days = (v - b - 1) // (a - b) + 1

print(days)