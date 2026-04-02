n = int(input())
for _ in range(n):
    data = input().split()
    x = data[1]
    y = int(data[0])
    for i in range(len(x)):
        print(x[i]*y,end="")
    print()
