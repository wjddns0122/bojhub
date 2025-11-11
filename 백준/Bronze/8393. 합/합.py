n = int(input())
result = 0

for i in range(n):
    i += 1
    result = result + i
    if i == n:
        break

print(result)