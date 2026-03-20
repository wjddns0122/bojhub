n, m = list(map(int, input().split()))

matrix_a = []
for i in range(n):
    matrix_a.append(list(map(int, input().split())))

for i in range(n):
    matrix_b_row = list(map(int, input().split()))
    for j in range(m):
        matrix_a[i][j] += matrix_b_row[j]

for row in matrix_a:
    print(*row)