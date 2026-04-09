n = int(input())
original_n = n  
count = 0

while True:
    sum_digits = (n // 10) + (n % 10)
    n = (n % 10) * 10 + (sum_digits % 10)
    count += 1
    if n == original_n:
        break

print(count)