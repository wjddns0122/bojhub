n = int(input())
array = list(map(int, input().split()))

m = max(array)

new_scores = [(x / m) * 100 for x in array]
new_average = sum(new_scores) / n

print(f"{new_average:.6f}")