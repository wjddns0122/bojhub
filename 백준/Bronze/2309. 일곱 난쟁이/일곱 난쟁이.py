from itertools import combinations

# 아홉 난쟁이의 키를 입력받기
dwarfs = [int(input()) for _ in range(9)]

# 모든 조합을 확인하여 일곱 난쟁이를 찾기
for combo in combinations(dwarfs, 7):
    if sum(combo) == 100:
        result = sorted(combo)  # 오름차순으로 정렬
        break

# 결과 출력
for height in result:
    print(height)