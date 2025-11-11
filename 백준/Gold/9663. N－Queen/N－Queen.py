def place_queens(row):
    global count  # 전역 변수 count 사용
    if row == N:  # 모든 퀸을 놓았으면
        count += 1  # 경우의 수 증가
        return
    for col in range(N):
        if not cols[col] and not diag1[row - col + (N - 1)] and not diag2[row + col]:  # 현재 위치에 퀸을 놓을 수 있으면
            # 현재 위치에 퀸을 놓는다
            cols[col] = True
            diag1[row - col + (N - 1)] = True
            diag2[row + col] = True

            # 다음 퀸을 놓기 위해 재귀 호출
            place_queens(row + 1)

            # 백트래킹: 퀸을 제거한다
            cols[col] = False
            diag1[row - col + (N - 1)] = False
            diag2[row + col] = False

N = int(input())

count = 0

cols = [False] * N           # 열
diag1 = [False] * (2 * N - 1)  # 대각선 (row - col)
diag2 = [False] * (2 * N - 1)  # 대각선 (row + col)

# 퀸을 놓기 시작
place_queens(0)

print(count)