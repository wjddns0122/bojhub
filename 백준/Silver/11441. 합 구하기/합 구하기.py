import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
psum = [0 for _ in range(n+1)]
for i in range(n):
    psum[i+1] = arr[i]
    psum[i+1] += psum[i]
m = int(input())
for _ in range(m):
    i, j = map(int, input().split())
    print(psum[j] - psum[i-1])