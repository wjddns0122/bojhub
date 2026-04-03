n = int(input())
count = 0


for i in range(n):
    word = input()
    # 그룹 단어인지 확인하는 로직 추가
    is_group_word = True
    seen = set()
    prev_char = ''

    for char in word:
        if char != prev_char:
            if char in seen:
                is_group_word = False
                break
            seen.add(char)
        prev_char = char
    if is_group_word:
        count += 1

print(count)
