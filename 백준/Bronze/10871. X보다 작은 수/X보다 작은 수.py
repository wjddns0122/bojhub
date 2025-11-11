n, x = map(int, input().split())
data = list(map(int, input().split()))

result = []

for value in data:
    if value < x:
        result.append(value)
        
print(" ".join(map(str, result)))