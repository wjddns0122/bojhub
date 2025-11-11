# 바구니의 개수 N과 역순으로 만들 작업의 개수 M 입력 받기
n, m = map(int, input().split())

# 1부터 N까지의 숫자를 가진 리스트 초기화
baskets = list(range(1, n + 1))

# M번의 작업 수행
for _ in range(m):
    # 역순으로 만들 범위 입력 받기
    i, j = map(int, input().split())
    # i에서 j까지의 범위를 역순으로 만들기
    baskets[i - 1:j] = reversed(baskets[i - 1:j])

# 결과 출력
print(" ".join(map(str, baskets)))