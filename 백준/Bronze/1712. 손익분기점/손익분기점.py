A, B, C = map(int, input().split())

if B >= C:
    print(-1)  # 손익분기점 없음
else:
    n = A // (C - B) + 1
    print(n)
