a = int(input())

arr = []
for _ in range(a):
    s = input()
    arr.append(s)

for i in range(len(arr)):
    x = arr[i]
    if len(x) > 1:
        print(f"{x[0]}{x[-1]}")
    else:
        print(x[0] * 2)