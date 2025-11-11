text = input().strip()  # 입력받은 문자열에서 공백 제거

char_counts = {}

# 각 문자의 빈도수 세기 (대소문자 구분 없이)
for char in text:
    char = char.upper()  # 모든 문자를 대문자로 변환
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

# 가장 많이 나온 문자와 그 빈도수 찾기
most_common_count = max(char_counts.values())
most_common_chars = [char for char, count in char_counts.items() if count == most_common_count]

# 결과 출력
if len(most_common_chars) > 1:
    print('?')
else:
    print(most_common_chars[0])