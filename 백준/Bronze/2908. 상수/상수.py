arr = input().split()
a = arr[0]
b = arr[1]
arr1 = []
arr2 = []

for i in range(len(a) - 1, -1, -1):
    arr1.append(a[i])

for i in range(len(b) -1, -1, -1):
    arr2.append(b[i])

result1 = int("".join(arr1))
result2 = int("".join(arr2))
if result1 > result2:
    print(result1)
else:
    print(result2)