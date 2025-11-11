n = input()

reversed_n = ''.join(reversed(n))

if n == reversed_n:
    print(int(1))
else:
    print(int(0))