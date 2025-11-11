h, m = map(int, input().split())
cooking_time = int(input())

m += cooking_time
while m >= 60:
    h += 1
    m -= 60
    if h == 24:
        h = 0
        
print(h, m)