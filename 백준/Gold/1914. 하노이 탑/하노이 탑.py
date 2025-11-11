def hanoi(n, a, target, c):
    if n == 1:
        print(a, target)
    else:
        hanoi(n - 1, a, c, target)
        print(a, target)
        hanoi(n - 1, c, target, a)
        
N = int(input())
K = (2 ** N) - 1
print(K)

if N <= 20:
    hanoi(N, 1, 3, 2)