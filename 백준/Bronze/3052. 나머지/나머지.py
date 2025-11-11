list = set()
count = 0

for _ in range(10):
    a = int(input())
    extra = a % 42
    list.add(extra)
    
    
print(len(list))