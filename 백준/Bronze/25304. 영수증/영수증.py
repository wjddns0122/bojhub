x = int(input())
n = int(input())
sum = 0
result = 0

for i in range(n):
    a, b = map(int, input().split())
    sum = a * b
    result += sum
    
if result == x:
    print("Yes")
else:
    print("No")