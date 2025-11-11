n = int(input())

for i in range(n):
    # 공백의 개수는 n - i - 1, 별의 개수는 i + 1
    result = " " * (n - i - 1) + "*" * (i + 1)
    print(result)