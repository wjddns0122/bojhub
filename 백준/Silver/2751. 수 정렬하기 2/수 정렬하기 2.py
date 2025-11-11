import sys
import random

# 입력받은 원소의 개수 n
n = int(sys.stdin.readline().strip())
array = []

for i in range(n):
    data = int(sys.stdin.readline().strip())  # 각 원소를 정수로 변환하여 추가
    array.append(data)

# 퀵 정렬 구현
def quick_sort(arr):
    if len(arr) <= 1:  # 기본 사례
        return arr
    # 랜덤 피벗 선택
    pivot = arr[random.randint(0, len(arr) - 1)]
    
    left = [x for x in arr if x < pivot]    # 피벗보다 작은 원소들
    middle = [x for x in arr if x == pivot]  # 피벗과 같은 원소들
    right = [x for x in arr if x > pivot]   # 피벗보다 큰 원소들
    
    # 재귀 호출
    return quick_sort(left) + middle + quick_sort(right)

# 퀵 정렬 수행
sorted_array = quick_sort(array)

# 정렬된 결과 출력
for num in sorted_array:
    print(num)