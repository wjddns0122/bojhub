import sys

# 여러 개의 테스트 케이스를 처리하기 위해 무한 루프 사용
for line in sys.stdin:
    # 입력받은 줄을 공백으로 나누어 A와 B로 변환
    A, B = map(int, line.split())
    # A와 B의 합을 출력
    print(A + B)