t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    result = a + b
    print("Case #%s: %d" % (i+1, result))