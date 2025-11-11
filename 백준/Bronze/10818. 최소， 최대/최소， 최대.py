n = int(input())
data = list(map(int, input().split()))  # map 객체를 리스트로 변환

# 최대값과 최소값을 찾기
a1 = max(data)
a2 = min(data)

print(a2, a1)