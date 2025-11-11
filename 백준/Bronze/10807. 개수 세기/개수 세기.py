n = int(input())
data = list(map(int, input().split()))
v = int(input())
count = 0

for _ in range(n):
    if data[_] == v:
        count += 1
        
print(count)