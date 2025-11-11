import sys
input = sys.stdin.readline

input_str = input().lstrip().rstrip()
cnt = 0

if len(input_str) == 0:
    print(0)
else:
    for i in input_str:
        if i == ' ':
            cnt += 1
    print(cnt+1)