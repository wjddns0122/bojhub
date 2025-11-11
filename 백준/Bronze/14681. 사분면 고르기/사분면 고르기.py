x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(int(1))
elif x < 0 and y > 0:
    print(int(2))
elif x < 0 and y < 0:
    print(int(3))
elif x > 0 and y < 0:
    print(int(4))