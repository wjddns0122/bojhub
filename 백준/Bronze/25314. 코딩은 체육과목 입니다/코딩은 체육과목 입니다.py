import sys

n = int(sys.stdin.readline())
if n % 4 == 0:
    result = n // 4
    sentence = "long"
    a = " ".join([sentence] * result)
    print(a, "int")