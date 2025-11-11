while True:
    a, b = map(int, input().split())
    result = a + b
    if a == b == 0:
        break
    print(result)