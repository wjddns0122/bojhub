n = int(input())
a, b = 0, 1  # F(0)=0, F(1)=1
for _ in range(n):
    a, b = b, a + b
print(a)