import sys

data = []

# sys.stdin으로부터 입력을 받습니다.
for line in sys.stdin:
    a = int(line.strip())  # 입력을 정수로 변환
    data.append(a)

if data:  # data가 비어있지 않은 경우
    max1 = max(data)  # 최대값 찾기
    index = data.index(max1)  # 최대값의 인덱스 찾기 (0부터 시작)

    print(max1)
    print(index + 1)  # 1부터 시작하는 인덱스로 출력
else:
    print("입력된 데이터가 없습니다.")